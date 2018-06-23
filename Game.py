''' 
The driver file of the program.
This is where the game is run and controlled.
'''

import time

import pygame

import Maze

pygame.init()

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
CAPTION = "PACMAN"

window_surface = pygame.display.set_mode( (WINDOW_HEIGHT , WINDOW_WIDTH) , 0 , 32 )
pygame.display.set_caption(CAPTION)
