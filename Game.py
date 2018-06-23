''' 
The driver file of the program.
This is where the game is run and controlled.
'''

import time

import pygame

import sys

import Maze

import Colors

pygame.init()

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700
CAPTION = "PACMAN"

window_surface = pygame.display.set_mode( ( WINDOW_WIDTH , WINDOW_HEIGHT) )
pygame.display.set_caption(CAPTION)

maze = Maze.Maze(".\\res\\levels\\1.json")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    window_surface.fill(Colors.BLACK)

    window_surface = maze.update_surface(window_surface)
    pygame.display.update()


