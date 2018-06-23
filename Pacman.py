"""
The class here contains information about pacman and its properties.
"""

import pygame

import os


class Pacman():
    
    def __init__(self , pos_x , pos_y):
        self.x = pos_x
        self.y = pos_y

        # initially it is not moving
        self.x_vel = 1
        self.y_vel = 0
        
        # l - left , u - up , r - right , d - down.
        self.direction = 'r'
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

    def update(self , window_surface):

        if self.frame_number >= (8 * self.frame_skip ):
            self.frame_number = 0

        image = self.images[self.direction][self.frame_number // self.frame_skip]
        position = [self.x , self.y]
        window_surface.blit(image , position)

        self.move()

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.frame_number += 1

        