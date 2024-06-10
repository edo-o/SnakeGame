import pygame
import sys
from pygame.math import Vector2
import random

class FRUIT:
    def __init__(self):
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x, self.y)
        #create x and y position for the fruit
        #draw a square

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175, 215, 70))
    pygame.display.update()
    clock.tick(60)