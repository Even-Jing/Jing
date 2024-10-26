import pygame
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the game window
WIDTH = 800
HEIGHT = 600
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Snake's initial position and size
snake_x = WIDTH / 2
snake_y = HEIGHT / 2
snake_size = 10

# Snake's movement speed
speed_x = 0
speed_y = 0

# Food position
food_x = round(random.randrange(0, WIDTH - snake_size) / 10.0) * 10.0
food_y = round(random.randrange(0, HEIGHT - snake_size) / 10.0) * 10.0

# Initialize snake's body
snake_body = []
snake_length = 1

# Set up game clock
clock = pygame.time.Clock()

# Main game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -snake_size
                speed_y = 0
            elif event.key == pygame.K_RIGHT:
                speed_x = snake_size
                speed_y = 0
            elif event.key == pygame.K_UP:
                speed_y = -snake_size
                speed_x = 0
            elif event.key == pygame.K_DOWN:
                speed_y = snake_size
                speed_x = 0

    # Move the snake
    snake_x += speed_x
    snake_y += speed_y

    # Check if snake ate the food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, WIDTH - snake_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, HEIGHT - snake_size) / 10.0) * 10.0
        snake_length += 1

    # Update snake's body
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Check if snake hit the wall or itself
    if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
        game_over = True
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over = True

    # Draw game elements
    game_window.fill(WHITE)
    for segment in snake_body:
        pygame.draw.rect(game_window, GREEN, [segment[0], segment[1], snake_size, snake_size])
    pygame.draw.rect(game_window, RED, [food_x, food_y, snake_size, snake_size])

    # Update display
    pygame.display.update()

    # Control game speed
    clock.tick(5)

# Quit the game
pygame.quit()
