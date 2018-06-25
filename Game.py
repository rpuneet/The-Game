''' 
The driver file of the program.
This is where the game is run and controlled.
'''

import pygame   # The library for graphics.

import Maze     # Contains information about the Maze.

import Colors   # Contains different colors for UI

import Pacman   # For holding informations about pacman.

import Ghost    # For holding information about each ghost.

import os       # For os.path.join and os.getcwd 

pygame.init()   # Initialising pygame

# Constants.
FPS = 144
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 900
CAPTION = "PACMAN"
LEVEL = 1
GHOST_RELEASE_DELAY = 5000
CELL_WIDTH = 24
CELL_HEIGHT = 24

# Utility Finctions

def check_win(maze):
    ''' 
    Check if there is any pellet left in the maze.
    Parameters -
        maze - Maze object which contains maze information
    '''
    for row in maze.matrix:
        for cell in row:
            if "pellet" in cell:
                return False
    
    return True

def release_ghost_in_maze(ghosts_in_maze , ghosts_not_in_maze):
    '''
    Releases ghosts in the maze after every 5 seconds.
    It transfers ghosts not in maze to ghost in maze and changes its in_maze value to True.

    Parameters-
        ghost_in_maze - list of ghosts that are in maze.
        ghost_not_in_maze - list of ghosts that are in ghost box.
    '''
    if pygame.time.get_ticks() >= (len(ghosts_in_maze) + 1) * GHOST_RELEASE_DELAY:
        ghost_to_release = ghosts_not_in_maze.pop()
        ghost_to_release.in_maze = True
        ghosts_in_maze.append(ghost_to_release)

def game_won():
    pygame.time.delay(2000)

def game_over():
    pygame.time.delay(2000)

def check_ghost_collision(pacman , ghost):
    pacman_x_index = round(pacman.x / CELL_WIDTH)
    pacman_y_index = round(pacman.y / CELL_HEIGHT)

    ghost_x_index = round(ghost.x / CELL_WIDTH)
    ghost_y_index = round(ghost.y / CELL_HEIGHT)

    if(ghost_x_index == pacman_x_index and ghost_y_index == pacman_y_index):
        return True

def check_ghosts_collision(pacman , ghosts_in_maze):
    for ghost in ghosts_in_maze:
        if check_ghost_collision(pacman , ghost):
            return True
    return False
    
    


# Initialising the screen.
window_surface = pygame.display.set_mode( ( WINDOW_WIDTH , WINDOW_HEIGHT) )
pygame.display.set_caption(CAPTION)

# Game Objects.
clock = pygame.time.Clock()
maze = Maze.Maze( os.path.join(os.getcwd() , "res" , "levels" , "{}.json".format(LEVEL)))
pacman = Pacman.Pacman(336 , 504)
ghosts_not_in_maze = [ Ghost.Ghost(
                        os.path.join(os.getcwd() , 'res' , 'tiles' , 'ghost-{}.gif'.format(ghost_name)),
                         13 * 24 , 13 * 24) for ghost_name in [ "sue",
                                                                "inky",
                                                                "pinky",
                                                                "blinky"]]
ghosts_in_maze = []

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
    for ghost in ghosts_not_in_maze:
        ghost.update(window_surface , maze)
    for ghost in ghosts_in_maze:
        ghost.update(window_surface , maze)


    # Update the screen.
    pygame.display.update()

    # Check for collision with ghost.
    if check_ghosts_collision(pacman , ghosts_in_maze):
        game_over()
        exit(0)

    # Check if all the pellets are gone.
    if check_win(maze):
        game_won()
        exit(0)

    # Release 1 ghost in the maze after every 5 second. if there is a ghost to release.
    if len(ghosts_not_in_maze) > 0:
        release_ghost_in_maze(ghosts_in_maze , ghosts_not_in_maze)


    clock.tick(FPS)     # Maintains the fps at a particular value.
