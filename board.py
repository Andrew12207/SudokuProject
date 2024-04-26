import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.rows = 9
        self.cols = 9
        self.cells = [[Cell(0, i, j, screen) for j in range(self.cols)] for i in range(self.rows)]
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None
        self.board = None
        self.sudoku = None
        self.final_sudoku = None
        self.initial_sudoku = None
        self.generate_board()
        self.cell_is_toggled = False
        self.toggled_cell_pos = None

    def generate_board(self):
        self.sudoku = SudokuGenerator(self.difficulty)
        self.sudoku.fill_values()
        self.final_sudoku = self.sudoku.get_board()
        self.sudoku.remove_cells()
        self.board = self.sudoku.get_board()
        self.initial_sudoku = self.sudoku.get_board()
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].set_cell_value(self.board[i][j])
        return self.final_sudoku

    def generate_initial_board(self):
        self.board = self.initial_sudoku
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].set_cell_value(self.board[i][j])
                self.cells[i][j].set_sketched_value(0)
        try:
            y = (self.toggled_cell_pos[0] + 30 + self.toggled_cell_pos[0] * 40)
            x = (self.toggled_cell_pos[1] + 135 + self.toggled_cell_pos[1] * 40)
            self.click(x, y)
        except:
            pass

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
                self.cells[self.toggled_cell_pos[0]][self.toggled_cell_pos[1]].toggle_selected()
                self.cells[row][col].toggle_selected()
                self.cells[row][col].draw()
                self.toggled_cell_pos = (row, col)
                self.cell_is_toggled = True
                return True
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

    def sketch(self, value):
        empty_cells = self.find_empty()
        if self.cell_is_toggled and self.toggled_cell_pos in empty_cells:
            self.cells[self.toggled_cell_pos[0]][self.toggled_cell_pos[1]].set_sketched_value(value)

    def place_number(self, value):
        value = self.cells[self.toggled_cell_pos[0]][self.toggled_cell_pos[1]].sketched_value
        empty_cells = self.find_empty()
        if self.cell_is_toggled and self.toggled_cell_pos in empty_cells:
            self.cells[self.toggled_cell_pos[0]][self.toggled_cell_pos[1]].set_cell_value(value)
            self.sudoku.board[self.toggled_cell_pos[0]][self.toggled_cell_pos[1]] = value
        y = (self.toggled_cell_pos[0]+30+self.toggled_cell_pos[0]*40)
        x = (self.toggled_cell_pos[1]+135+self.toggled_cell_pos[1]*40)
        self.click(x, y)

    def select(self, row, col):
        self.selected_cell = (row, col)
        return self.selected_cell

    def find_empty(self):
        empty_cells = []
        for row in range(9):
            for col in range(9):
                if self.initial_sudoku[row][col] not in range(1, 10):
                    empty_cells.append((row, col))
        return empty_cells

    def find_current_empty(self):
        empty_cells = []
        for row in range(9):
            for col in range(9):
                if self.sudoku.get_board()[row][col] not in range(1, 10):
                    empty_cells.append((row, col))
        return empty_cells

    def is_full(self):
        empty_cells = self.find_current_empty()
        if len(empty_cells) == 0:
            return True
        else:
            return False

    def check_board(self):
        if self.sudoku.get_board() == self.final_sudoku:
            return True
        else:
            return False
