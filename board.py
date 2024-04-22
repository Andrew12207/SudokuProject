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
