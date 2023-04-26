import pygame
from math import sin, cos, radians, sqrt
import numpy as np

class Entity:
    
    def __init__(self, screen, position_x, position_y, vision_angle):
        self.alive = True
        self.radius = 10
        self.position_x = position_x
        self.position_y = position_y
        self.screen = screen
        self.vision_angle = vision_angle
        self.target_vision_angle = self.vision_angle

    def getPosition(self):
        return [self.position_x, self.position_y]

    def move(self):
        if self.vision_angle == self.target_vision_angle:
            if np.random.randint(0, 2):
                self.target_vision_angle += np.random.randint(10, 21)
            else:
                self.target_vision_angle -= np.random.randint(10, 21)

        if self.vision_angle > self.target_vision_angle:
            self.vision_angle -= 1        
        elif self.vision_angle < self.target_vision_angle:
            self.vision_angle += 1

        self.position_x += cos(radians(self.vision_angle))
        self.position_y -= sin(radians(self.vision_angle))

    def draw(self):
        pygame.draw.circle(self.screen, "green", self.getPosition(), self.radius)
        pygame.draw.line(self.screen, "green", self.getPosition(), self.frontLine(), 2)
    
    def frontLine(self):
        x = self.position_x + cos(radians(self.vision_angle)) * 20
        y = self.position_y - sin(radians(self.vision_angle)) * 20
        return [x, y]

    def distanceBetween(self, position_x, position_y):
        x_difference = self.position_x - position_x
        y_difference = self.position_y - position_y
        return sqrt(x_difference ** 2 + y_difference ** 2)