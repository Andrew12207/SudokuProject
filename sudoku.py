import pygame
import sys

from sudoku_generator import SudokuGenerator
from board import Board

SCREEN_SIZE = (665, 716)
BUTTON_COLOR = (210, 180, 140)
BUTTON_TEXT_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
GRID_COLOR = (50, 50, 150)
BOARD_MARGIN = 10
BOARD_HEIGHT = SCREEN_SIZE[1] * 9 // 10 - 2 * BOARD_MARGIN
BOARD_WIDTH = SCREEN_SIZE[0] - 2 * BOARD_MARGIN
CELL_SIZE = BOARD_WIDTH // 9
BOARD_DIMENSIONS = (BOARD_WIDTH, CELL_SIZE * 9)
BOARD_OFFSET_X = BOARD_MARGIN
BOARD_OFFSET_Y = BOARD_MARGIN

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
font = pygame.font.Font(None, 36)

current_board = None
initial_board = None
in_game = False


def draw_button(text, x, y, w=150, h=50):
    pygame.draw.rect(screen, BUTTON_COLOR, (x, y, w, h))
    text_surf = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surf.get_rect(center=(x + w / 2, y + h / 2))
    screen.blit(text_surf, text_rect)
    return pygame.Rect(x, y, w, h)


def handle_mouse_click(pos):
    global current_board, initial_board, in_game
    if not in_game:

        if easy_btn.collidepoint(pos):
            current_board = Board(BOARD_OFFSET_X, BOARD_OFFSET_Y, screen, 30)
            initial_board = current_board
            in_game = True
        elif medium_btn.collidepoint(pos):
            current_board = Board(BOARD_OFFSET_X, BOARD_OFFSET_Y, screen, 40)
            initial_board = current_board
            in_game = True
        elif hard_btn.collidepoint(pos):
            current_board = Board(BOARD_OFFSET_X, BOARD_OFFSET_Y, screen, 50)
            initial_board = current_board
            in_game = True
    else:
        reset_btn = draw_button("RESET", SCREEN_SIZE[0] // 2 - 225, 650)
        restart_btn = draw_button("RESTART", SCREEN_SIZE[0] // 2 - 75, 650)
        exit_btn = draw_button("EXIT", SCREEN_SIZE[0] // 2 + 75, 650)

        if reset_btn.collidepoint(pos):
            current_board = initial_board
        elif restart_btn.collidepoint(pos):
            in_game = False
        elif exit_btn.collidepoint(pos):
            pygame.quit()
            sys.exit()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click(pygame.mouse.get_pos())

    screen.fill(BACKGROUND_COLOR)

    if not in_game:
        welcome_text = font.render("Welcome to Sudoku", True, (0, 0, 0))
        welcome_text_rect = welcome_text.get_rect(center=(SCREEN_SIZE[0] // 2, 150))
        screen.blit(welcome_text, welcome_text_rect)

        select_mode_text = font.render("Select game mode:", True, (0, 0, 0))
        select_mode_text_rect = select_mode_text.get_rect(center=(SCREEN_SIZE[0] // 2, 250))
        screen.blit(select_mode_text, select_mode_text_rect)

        easy_btn = draw_button("EASY", SCREEN_SIZE[0] // 2 - 75, 325)
        medium_btn = draw_button("MEDIUM", SCREEN_SIZE[0] // 2 - 75, 400)
        hard_btn = draw_button("HARD", SCREEN_SIZE[0] // 2 - 75, 475)
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click(pygame.mouse.get_pos())
    else:

        current_board.draw()

        draw_button("RESET", SCREEN_SIZE[0] // 2 - 225, 650)
        draw_button("RESTART", SCREEN_SIZE[0] // 2 - 75, 650)
        draw_button("EXIT", SCREEN_SIZE[0] // 2 + 75, 650)

    pygame.display.flip()

pygame.quit()