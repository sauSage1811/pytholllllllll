import pygame
import time
import random

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
width = 600
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rắn săn mồi")

# Màu sắc
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Kích thước khối
block_size = 20
snake_speed = 10

# Font
font = pygame.font.SysFont(None, 35)

def message(msg, color):
    text = font.render(msg, True, color)
    window.blit(text, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            window.fill(white)
            message("Ban thua! Nhan Q de thoat, C de choi lai", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        window.fill(white)
        pygame.draw.rect(window, green, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        for segment in snake_List:
            pygame.draw.rect(window, black, [segment[0], segment[1], block_size, block_size])

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
