''' 
The driver file of the program.
This is where the game is run and controlled.
'''

import time

import pygame

import sys

import Maze

import Colors

import Pacman

pygame.init()

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700
CAPTION = "PACMAN"

window_surface = pygame.display.set_mode( ( WINDOW_WIDTH , WINDOW_HEIGHT) )
pygame.display.set_caption(CAPTION)

clock = pygame.time.Clock()
maze = Maze.Maze(".\\res\\levels\\1.json")
pacman = Pacman.Pacman(5 * 24,17 * 24)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pacman.change_direction('l' , maze)
            
            if event.key == pygame.K_RIGHT:
                pacman.change_direction('r' , maze)
            
            if event.key == pygame.K_UP:
                pacman.change_direction('u' , maze)
            
            if event.key == pygame.K_DOWN:
                pacman.change_direction('d' , maze)


    window_surface.fill(Colors.BLACK)

    maze.update(window_surface)
    pacman.update(window_surface , maze)

    pygame.display.update()
    clock.tick(144)


