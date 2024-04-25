import pygame
import sys
from board import Board

SCREEN_SIZE = (650, 600)
BUTTON_COLOR = (210, 180, 140)
BUTTON_TEXT_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
GRID_COLOR = (50, 50, 150)
BOARD_MARGIN = 10
BOARD_HEIGHT = 390
BOARD_WIDTH = SCREEN_SIZE[0] - 2 * BOARD_MARGIN - 135
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
        while not in_game:
            if easy_btn.collidepoint(pos):
                current_board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, 1)
                initial_board = current_board
                current_board.draw()
                in_game = True
            elif medium_btn.collidepoint(pos):
                current_board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, 40)
                initial_board = current_board
                current_board.draw()
                in_game = True
            elif hard_btn.collidepoint(pos):
                current_board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, 50)
                initial_board = current_board
                current_board.draw()
                in_game = True
            else:
                break
    else:
        while in_game:
            if current_board.click(pos[0], pos[1]):
                break
            elif restart_btn.collidepoint(pos):
                current_board = None
                in_game = False
            elif reset_btn.collidepoint(pos):
                current_board.generate_initial_board()
                current_board.draw()
                break
            elif exit_btn.collidepoint(pos):
                pygame.quit()
                sys.exit()
            else:
                break


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            handle_mouse_click(pygame.mouse.get_pos())

        if event.type == pygame.KEYUP:
            if current_board.cell_is_toggled:
                pos = pygame.mouse.get_pos()
                self_selected_cell = current_board.select(pos[0], pos[1])
                if event.key == pygame.K_1:
                    current_board.place_number(1)
                    current_board.draw()
                elif event.key == pygame.K_2:
                    current_board.place_number(2)
                    current_board.draw()
                elif event.key == pygame.K_3:
                    current_board.place_number(3)
                    current_board.draw()
                elif event.key == pygame.K_4:
                    current_board.place_number(4)
                    current_board.draw()
                elif event.key == pygame.K_5:
                    current_board.place_number(5)
                    current_board.draw()
                elif event.key == pygame.K_6:
                    current_board.place_number(6)
                    current_board.draw()
                elif event.key == pygame.K_7:
                    current_board.place_number(7)
                    current_board.draw()
                elif event.key == pygame.K_8:
                    current_board.place_number(8)
                    current_board.draw()
                elif event.key == pygame.K_9:
                    current_board.place_number(9)
                    current_board.draw()

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
    else:
        current_board.draw()
        reset_btn = draw_button("RESET", SCREEN_SIZE[0] // 2 - 225, 400, 125)
        restart_btn = draw_button("RESTART", SCREEN_SIZE[0] // 2 - 75, 400, 125)
        exit_btn = draw_button("EXIT", SCREEN_SIZE[0] // 2 + 75, 400, 125)

        if current_board.is_full():
            if current_board.check_board():
                print("You won")
                current_board = None
                in_game = False
            else:
                print("You lost")
                current_board = None
                in_game = False

    pygame.display.flip()

pygame.quit()