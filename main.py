import entidade

import pygame
from math import sin,cos,tan,radians, pi


# pygame setup
pygame.init()
x = 1280
y = 720
screen = pygame.display.set_mode((x, y))
clock = pygame.time.Clock()
running = True


# Variaveis de entidades

listaEnt = []

# Criando Variaveis de entidades

qntEntidades = 1
for i in range(qntEntidades):
    posX = x / 2 + cos(radians((360 / qntEntidades) * i)) * 299
    posY = y / 2 - sin(radians((360 / qntEntidades) * i)) * 299

    print (posX,posY)

    listaEnt.append(entidade.entidade(screen,posX,posY, 180 + (360 / qntEntidades) * i))


# Ciclo do jogo
while running:
    # Checa a stack de eventos
    # pygame.QUIT é o evento de clicar no X

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # apaga o ultimo frame enxendo a tela de preto
    screen.fill("black")

    # Desenhando
    pygame.draw.circle(screen,"white", [x / 2, y / 2], 300)
    
    for ent in listaEnt:
        ent.draw()
        if ent.calculaDistancia(x / 2, y / 2) < 300:
            ent.randomMove()

    # Trocando o buffer para aparecer oque foi desenhado
    pygame.display.flip()

    clock.tick(60)  # Limite de FPS

pygame.quit()