import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator


class Board:
    global final_sudoku

    def __init__(self, width, height, screen, difficulty):
        self.rows = 9
        self.cols = 9
        self.cells = [[Cell(0, i, j, screen) for j in range(self.cols)] for i in range(self.rows)]
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None
        self.generate_board()
        self.cell_is_toggled = False
        self.toggled_cell_pos = None

    def generate_board(self):
        sudoku = SudokuGenerator(self.difficulty)
        final_sudoku = sudoku.fill_values()
        sudoku.remove_cells()
        board = sudoku.get_board()
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].set_cell_value(board[i][j])
        return final_sudoku

    def draw(self):
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0 and i != 9:
                thickness = 5
            else:
                thickness = 1
            pygame.draw.line(self.screen, (0, 0, 0), (i*40+135, 30), (i*40+135, self.height), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (135, i*40+30), (self.width, i*40+30), thickness)
        pygame.draw.line(self.screen, (0, 0, 0), (135, 30), (135, self.height), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (133, 30), (self.width, 30), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (495, 28), (495, self.height), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (133, 390), (self.width+2, 390), 5)
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col].draw()

    def click(self, x, y):
        cell_size = (self.width-135) / 9
        row = int((y-30) // cell_size)
        col = int((x-135) // cell_size)
        if 0 <= row < 9 and 0 <= col < 9:
            if self.cell_is_toggled and self.toggled_cell_pos != (row, col):
                return False
            elif self.cell_is_toggled and self.toggled_cell_pos == (row, col):
                self.cells[row][col].toggle_selected()
                self.toggled_cell_pos = None
                self.cell_is_toggled = False
                return False
            else:
                self.cells[row][col].toggle_selected()
                self.cells[row][col].draw()
                self.toggled_cell_pos = (row, col)
                self.cell_is_toggled = True
                return True
        else:
            return False

    def clear(self):
        if self.selected_cell:
            self.cells[self.selected_cell[0]][self.selected_cell[1]].set_cell_value(0)

    def sketch(self, value):
        if self.selected_cell:
            self.cells[self.selected_cell[0]][self.selected_cell[1]].set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell:
            self.cells[self.selected_cell[0]][self.selected_cell[1]].set_cell_value(value)

    def select(self, row, col):
        self.selected_cell = (row, col)
        return self.selected_cell

    def is_full(self):
        pass

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col] not in range(1, 10):
                    return row, col


    def check_board(self):
        if self.get_board == final_sudoku.get_board:
            return True
        else:
            return False

    def update_board(self):
        new_value = current_board.self_selected_cell.set_cell_value(1)
        current_board.place_number(new_value)
        current_board.draw()


    '''def reset_to_original(self):
        if check_board == False:
           ='''



