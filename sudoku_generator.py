from random import randint as rand


class SudokuGenerator:
    def __init__(self, removed_cells, row_length=9):
        self.row_length = row_length
        self.board = []
        for i in range(0, row_length):
            temp = []
            for j in range(0, row_length):
                temp.append(0)
            self.board.append(temp)
        self.removed_cells = removed_cells
        self.box_length = int(row_length**0.5)

    def get_board(self):
        returned_board = []
        mid_board = []
        for i in range(0, self.row_length):
            for j in range(0, self.row_length):
                mid_board.append(self.board[i][j])
            returned_board.append(mid_board)
            mid_board = []
        return returned_board

    def print_board(self):
        for i in range(0, self.row_length):
            for j in range(0, self.row_length):
                print(self.board[i][j], end='')
            print("\n")

    def valid_in_row(self, row, num):
        if num in self.board[row]:
            return False
        else:
            return True

    def valid_in_col(self, col, num):
        for i in range(0, self.row_length):
            if self.board[i][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        row_index = (row_start // 3) * 3
        col_index = (col_start // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[row_index + i][col_index + j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num):
            return True
        else:
            return False

    def fill_box(self, row_start, col_start):
        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                while True:
                    val = rand(1, 9)
                    if self.valid_in_box(row_start, col_start, val):
                        self.board[i][j] = val
                        break

    def fill_diagonal(self):
        for i in range(3):
            self.fill_box(i*3, i*3)

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        i = 0
        while i < self.removed_cells:
            row = rand(0, 8)
            col = rand(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                i += 1


    def generate_sudoku(size, removed):
        sudoku = SudokuGenerator(size, removed)
        sudoku.fill_values()
        board = sudoku.get_board()
        sudoku.remove_cells()
        board = sudoku.get_board()
        return board
