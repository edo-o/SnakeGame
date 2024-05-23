import pygame
import sys
import random


pygame.init()

#Create the screen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
SNAKE_SPEED = 15

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

#framerate
clock = pygame.time.Clock()
fps = 15

#colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = [0, 0]
food_pos = [random.randrange(1, (SCREEN_WIDTH//BLOCK_SIZE)) * BLOCK_SIZE, random.randrange(1, (SCREEN_HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]
food_spawn = True

#game loop
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_w]:
                snake_speed = [0, -BLOCK_SIZE]
            if keys[pygame.K_s]:
                snake_speed = [0, BLOCK_SIZE]
            if keys[pygame.K_a]:
                snake_speed = [-BLOCK_SIZE, 0]
            if keys[pygame.K_d]:
                snake_speed = [BLOCK_SIZE, 0]

    snake_pos[0][0] += snake_speed[0]
    snake_pos[0][1] += snake_speed[1]

    #game over conditions
    if snake_pos[0][0] >= SCREEN_WIDTH or snake_pos[0][0] < 0 or snake_pos[0][1] >= SCREEN_HEIGHT or snake_pos[0][1] < 0:
        running = False

    if snake_pos[0] in snake_pos[1:]:
        running = False

    #check if snake has eaten the food
    if snake_pos[0] == food_pos:
        food_spawn = False
        snake_pos.append([])  # Add a new segment to the snake

    # Spawn new food if needed
    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH//BLOCK_SIZE)) * BLOCK_SIZE, random.randrange(1, (SCREEN_HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]
        food_spawn = True

    #when snake eats the food
    if len(snake_pos) > 1:
        if snake_pos[0] == food_pos:
            food_spawn = False
        else:
            snake_pos.pop()

        if snake_pos[0] in snake_pos[1:]:
            running = False

    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH//BLOCK_SIZE)) * BLOCK_SIZE, random.randrange(1, (SCREEN_HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]
    food_spawn = True

    #draw snake and food

    for pos in snake_pos:
        if len(pos) >= 2:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

    if len(food_pos) >= 2:
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.update()

    clock.tick(fps)

pygame.quit()