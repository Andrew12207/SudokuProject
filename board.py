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
        self.generate_board()

    def generate_board(self):
        sudoku = SudokuGenerator(self.difficulty)
        sudoku.fill_values()
        sudoku.remove_cells()
        board = sudoku.get_board()
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].set_cell_value(board[i][j])

    def draw(self):
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(self.screen, (0, 0, 0), (i * self.width / 9, 0), (i * self.width / 9, self.height),
                             thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.height / 9), (self.width, i * self.height / 9),
                             thickness)

        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col].draw()

def click(self, x, y):
    cell_size = self.width / 9
    row = y // cell_size
    col = x // cell_size
    if 0 <= row < 9 and 0 <= col < 9:
        self.cells[row][col].toggle_selected()
        return row, col
    else:
        return None

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

