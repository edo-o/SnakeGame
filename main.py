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
fps = 60

#colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

snake_pos = [100, 50], [90, 50], [80, 50]
snake_speed = [0, BLOCK_SIZE]
food_pos = [random.randrange(1, (SCREEN_WIDTH//BLOCK_SIZE)) * BLOCK_SIZE, random.randrange(1, (SCREEN_HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]
food_spawn = True





pygame.display.update()

pygame.quit()