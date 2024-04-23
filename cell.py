import pygame


class Cell:
    def __init__(self, value, row, col, screen, cell_size=60):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.cell_size = cell_size
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        font = pygame.font.Font(None, 36)
        x = self.col * self.cell_size
        y = self.row * self.cell_size

        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + 20, y + (self.cell_size - text.get_height()) / 2))
        elif self.sketched_value != 0:
            text = font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(text, (x + 5, y + 5))

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, self.cell_size, self.cell_size), 3)
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), (x, y, self.cell_size, self.cell_size), 1)
    def toggle_selected(self):
    self.selected = not self.selected
