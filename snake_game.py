import pygame
import random
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


pygame.init()

WIDTH = 600
HEIGHT = 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Safe image loading
def load_image(filename):
    if os.path.exists(filename):
        img = pygame.image.load(filename)
        img = pygame.transform.scale(img, (BLOCK, BLOCK))
        return img
    else:
        return None

snake_img = load_image("friend1.png")
food_img = load_image("friend2.png")

def draw_snake(snake_list):
    for block in snake_list:
        if snake_img:
            screen.blit(snake_img, (block[0], block[1]))
        else:
            pygame.draw.rect(screen, (0,255,0), [block[0], block[1], BLOCK, BLOCK])

def show_score(score):
    value = font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [10, 10])

def game():
    x = WIDTH // 2
    y = HEIGHT // 2
    dx = 0
    dy = 0

    snake = []
    length = 1
    score = 0

    food_x = random.randrange(0, WIDTH - BLOCK, BLOCK)
    food_y = random.randrange(0, HEIGHT - BLOCK, BLOCK)

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -BLOCK
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -BLOCK
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = BLOCK
                    dx = 0

        x += dx
        y += dy

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            running = False

        screen.fill(BLACK)

        # Draw food
        if food_img:
            screen.blit(food_img, (food_x, food_y))
        else:
            pygame.draw.rect(screen, (255,0,0), [food_x, food_y, BLOCK, BLOCK])

        snake_head = [x, y]
        snake.append(snake_head)

        if len(snake) > length:
            del snake[0]

        for block in snake[:-1]:
            if block == snake_head:
                running = False

        draw_snake(snake)
        show_score(score)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK, BLOCK)
            food_y = random.randrange(0, HEIGHT - BLOCK, BLOCK)
            length += 1
            score += 1

        clock.tick(10)

    pygame.quit()
    sys.exit()

game()
