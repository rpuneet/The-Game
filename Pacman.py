"""
The class here contains information about pacman and its properties.
"""

import pygame

import os

from math import *

class Pacman():
    
    def __init__(self , pos_x , pos_y):
        self.x = pos_x
        self.y = pos_y

        # initially it is not moving
        self.x_vel = -1
        self.y_vel = 0
        
        # l - left , u - up , r - right , d - down.
        self.direction = 'l'
        # frame number goes from 1 to 8 to load the respective image on screen for animation
        self.frame_number = 0
        # frame skip is the number of frames to skip before drawing the next sprite.
        self.frame_skip = 10
        
        self.images = self.get_images()


    def get_images(self):
        path = os.path.join(os.getcwd() , "res" , "sprite")
        images = {'l':[] , 'r':[] , 'd':[] , 'u':[]}
        
        for i in range(1 ,9):
            for dir in images:
                images[dir].append(pygame.image.load(os.path.join(path , "pacman-{} {}.gif".format(dir , i))).convert())
        return images

    def update(self , window_surface , maze):

        if self.frame_number >= (8 * self.frame_skip ):
            self.frame_number = 0

        image = self.images[self.direction][self.frame_number // self.frame_skip]
        position = [self.x , self.y]
        window_surface.blit(image , position)

        self.move(maze)

    def get_index_maze(self , pos_x , pos_y):
        x_index , y_index = 0 , 0
        
        if self.x_vel == 1:
            x_index = ceil(pos_x/24)
        else:
            x_index = floor(pos_x/24)
        
        if self.y_vel == 1:
            y_index = ceil(pos_y/24)
        else:
            y_index = floor(pos_y/24)

        return x_index , y_index


    def move(self , maze):
        new_x = self.x + self.x_vel
        new_y = self.y + self.y_vel

        if new_x < 24:
            new_x = 24 * ( maze.x_length - 1)

        if new_x > 24 * ( maze.x_length - 1):
            new_x = 24
        
        x_index , y_index = self.get_index_maze(new_x , new_y)
        #print(self.x , self.y , x_index , y_index)
        if "wall" not in maze.matrix[y_index][x_index]:
            self.x = new_x
            self.y = new_y

        self.frame_number += 1

    def change_direction(self , dir , maze):
        index_x = round(self.x / 24)
        index_y = round(self.y / 24)
        
        
        if dir == 'l':
            if "wall" in maze.matrix[index_y][index_x - 1]:
                return
            self.x_vel = -1
            self.y_vel = 0
            self.y = index_y * 24
            self.direction = dir

        elif dir == 'r':
            if "wall" in maze.matrix[index_y][index_x + 1]:
                return
            self.x_vel = 1
            self.y_vel = 0
            self.y = index_y * 24
            self.direction = dir

        elif dir == 'd':
            if "wall" in maze.matrix[index_y + 1][index_x]:
                return
            self.x_vel = 0
            self.y_vel = 1
            self.x = index_x * 24
            self.direction = dir
        
        elif dir == 'u':
            if "wall" in maze.matrix[index_y - 1][index_x]:
                return
            self.x_vel = 0
            self.y_vel = -1
            self.x = index_x * 24
            self.direction = dir

        else:
            raise Exception("Incorrect direction.")