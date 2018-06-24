''' 
The driver file of the program.
This is where the game is run and controlled.
'''

import pygame   # The library for graphics.

import Maze     # Contains information about the Maze.

import Colors   # Contains different colors for UI

import Pacman   # For holding informations about pacman.

import Pallete  # For holding pallete information

import os       # For os.path.join and os.getcwd 

pygame.init()   # Initialising pygame

# Constants.
FPS = 144
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700
CAPTION = "PACMAN"
LEVEL = 1

# Initialising the screen.
window_surface = pygame.display.set_mode( ( WINDOW_WIDTH , WINDOW_HEIGHT) )
pygame.display.set_caption(CAPTION)

# Game Objects.
clock = pygame.time.Clock()
maze = Maze.Maze(os.path.join(os.getcwd() , "res" , "levels" , "{}.json".format(LEVEL)) )
pacman = Pacman.Pacman(336 , 504)

# Game Loop -
while True:
    for event in pygame.event.get():
        # Exit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        # If a key is pressed, change direction of Pacman.
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

    # Updating different objects in the game
    maze.update(window_surface)
    pacman.update(window_surface , maze)

    # Update the screen.
    pygame.display.update()

    clock.tick(FPS)     # Maintains the fps at a particular value.


