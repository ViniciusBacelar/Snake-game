import sys
import pygame
from functions import *
from functions import Button
from pygame.locals import *

pygame.init()

SCREEN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Menu")

BG = pygame.image.load(
    "C:\\Users\\vinic\\OneDrive\\Documentos\\Prog\\python\\Snake-game\\assets\\snake.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("C:\\Users\\vinic\\OneDrive\\Documentos\\Prog\\python\\Snake-game\\assets\\Pixel.ttf", size)


def play():
    while True:
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3

        pygame.init()
        pygame.display.set_caption('Snake')
        screen = pygame.display.set_mode((600, 600))
        fps = pygame.time.Clock()
        snake = [(200, 200), (210, 200), (220, 200)]
        snake_skin = pygame.Surface((10, 10))
        snake_skin.fill((0, 255, 0))  # White
        apple_pos = on_grid_random()
        apple = pygame.Surface((10, 10))
        apple.fill((0, 255, 0))
        my_direction = LEFT
        font = pygame.font.Font(
            'C:\\Users\\vinic\\OneDrive\\Documentos\\Prog\\python\\Snake-game\\assets\\Pixel.ttf', 18)
        scoreboard = 0
        init_game = True
        while init_game:
            fps.tick(15)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_UP and my_direction != DOWN:
                        my_direction = UP
                    if event.key == K_DOWN and my_direction != UP:
                        my_direction = DOWN
                    if event.key == K_LEFT and my_direction != RIGHT:
                        my_direction = LEFT
                    if event.key == K_RIGHT and my_direction != LEFT:
                        my_direction = RIGHT

            if collision(snake[0], apple_pos):
                apple_pos = on_grid_random()
                snake.append((0, 0))
                scoreboard = scoreboard + 1

            # Check if snake collided with boundaries
            if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
                init_game = False

            # Check if the snake has hit itself
            for i in range(1, len(snake) - 1):
                if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                    init_game = False

            if not init_game:
                init_game = False

            for i in range(len(snake) - 1, 0, -1):
                snake[i] = (snake[i-1][0], snake[i-1][1])

            # Actually make the snake move.
            if my_direction == UP:
                snake[0] = (snake[0][0], snake[0][1] - 10)
            if my_direction == DOWN:
                snake[0] = (snake[0][0], snake[0][1] + 10)
            if my_direction == RIGHT:
                snake[0] = (snake[0][0] + 10, snake[0][1])
            if my_direction == LEFT:
                snake[0] = (snake[0][0] - 10, snake[0][1])

            screen.fill((0, 0, 0))
            screen.blit(apple, apple_pos)

            for x in range(0, 600, 10):  # Draw vertical lines
                pygame.draw.line(screen, (0, 50, 0), (x, 0), (x, 600))
            for y in range(0, 600, 10):  # Draw vertical lines
                pygame.draw.line(screen, (0, 50, 0), (0, y), (600, y))

            score(screen, scoreboard, font)

            for pos in snake:
                screen.blit(snake_skin, pos)

            pygame.display.update()

        while not init_game:
            def end_menu():
                while True:
                    SCREEN.fill((0, 0, 0))
                    MENU_MOUSE_POS = pygame.mouse.get_pos()
                    MENU_TEXT = get_font(75).render(
                        "GAME OVER", True, (250, 0, 0))
                    MENU_RECT = MENU_TEXT.get_rect(center=(300, 250))
                    RESTART_BUTTON = Button(image=None, pos=(300, 300),
                                            text_input="RESTART GAME", font=get_font(40), base_color=(200, 0, 0), hovering_color="Green")
                    QUIT_BUTTON = Button(image=None, pos=(300, 340),
                                         text_input="QUIT", font=get_font(40), base_color=(200, 0, 0), hovering_color="Green")
                    CREATORS = Button(image=None, pos=(300, 550),
                                      text_input="BY VINICIUS BACELAR E DAVID TAVARES", font=get_font(20), base_color=(200, 0, 0), hovering_color="Green")

                    SCREEN.blit(MENU_TEXT, MENU_RECT)

                    for button in [RESTART_BUTTON, QUIT_BUTTON, CREATORS]:
                        button.changeColor(MENU_MOUSE_POS)
                        button.update(SCREEN)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if RESTART_BUTTON.checkForInput(MENU_MOUSE_POS):
                                play()
                            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                                pygame.quit()
                                sys.exit()

                    pygame.display.update()

            end_menu()


def main_menu():
    while True:
        SCREEN.blit(pygame.transform.scale(BG, (200, 150)), (200, 40))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(75).render("SNAKE GAME", True, (0, 150, 0))
        MENU_RECT = MENU_TEXT.get_rect(center=(center_position, 250))
        PLAY_BUTTON = Button(image=None, pos=(center_position, center_position),
                             text_input="START GAME", font=get_font(40), base_color=(200, 0, 0), hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(center_position, 340),
                             text_input="QUIT", font=get_font(40), base_color=(200, 0, 0), hovering_color="Green")
        CREATORS = Button(image=None, pos=(center_position, 550),
                          text_input="BY VINICIUS BACELAR E DAVID TAVARES", font=get_font(20), base_color=(200, 0, 0), hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON, CREATORS]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
