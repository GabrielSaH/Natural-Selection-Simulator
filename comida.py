import numpy as np
import pygame
from math import cos, sin

class comida:
    def __init__(self, screen, raioArena, posicaoInicial):
        raioComida = np.random.randint(10,raioArena * (4/5))
        anguloComida = np.random.randint(0,361)
        self.x = cos(anguloComida) * raioComida + posicaoInicial[0]
        self.y = posicaoInicial[1] - sin(anguloComida) * raioComida
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, "orange", [self.x,self.y], 5)
