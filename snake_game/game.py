import pygame

from snake_game.config_reader import load_config
from snake_game.food import Food
from snake_game.snake import Snake


def main():
    config = load_config()

    # Настройки экрана
    WIDTH = int(config["SCREEN"]["WIDTH"])
    HEIGHT = int(config["SCREEN"]["HEIGHT"])
    BLOCK_SIZE = int(config["GAME"]["BLOCK_SIZE"])
    FPS = int(config["GAME"]["FPS"])

    # Инициализация pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(config["GAME"]["TITLE"])
    clock = pygame.time.Clock()

    # Настройки игровых объектов
    SNAKE_COLOR = str(config["SNAKE"]["SNAKE_COLOR"])
    FOOD_COLOR = str(config["FOOD"]["FOOD_COLOR"])

    # Игра
    snake = Snake((100, 100), BLOCK_SIZE)
    food = Food(WIDTH, HEIGHT, BLOCK_SIZE)
    score = 0

    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обработка ввода
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake.set_direction((0, -BLOCK_SIZE))
        if keys[pygame.K_DOWN]:
            snake.set_direction((0, BLOCK_SIZE))
        if keys[pygame.K_LEFT]:
            snake.set_direction((-BLOCK_SIZE, 0))
        if keys[pygame.K_RIGHT]:
            snake.set_direction((BLOCK_SIZE, 0))

        # Обновление змейки
        snake.move()

        # Проверка столкновений
        if snake.has_collided(WIDTH, HEIGHT):
            print(f"Game Over! Your score: {score}")
            running = False

        # Проверка еды
        if snake.body[0] == food.position:
            snake.grow()
            food.generate()
            score += 1

        # Отрисовка
        screen.fill("black")
        snake.draw(screen, SNAKE_COLOR)
        food.draw(screen, FOOD_COLOR)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
