import entidade
import pygameHelpers
import comida

import pygame
from math import sin,cos,tan,radians, pi


# pygame setup
pygame.init()
x = 1280
y = 720
screen = pygame.display.set_mode((x, y))
clock = pygame.time.Clock()
running = True


# Criando Variaveis de entidades
listaEnt = []

qntEntidades = 3000
for i in range(qntEntidades):
    posX = x / 2 + cos(radians((360 / qntEntidades) * i)) * 299
    posY = y / 2 - sin(radians((360 / qntEntidades) * i)) * 299

    listaEnt.append(entidade.entidade(screen,posX,posY, 180 + (360 / qntEntidades) * i))

# Criando variaveis de comida
listaComida = []

qntComida = 60
for c in range(qntComida):
    listaComida.append(comida.comida(screen, 300, [x/2, y/2]))


# Ciclo do jogo
while running:
    # Checa a stack de eventos
    # pygame.QUIT é o evento de clicar no X


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Configurando pause
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygameHelpers.pause(screen)         

    # apaga o ultimo frame enxendo a tela de preto
    screen.fill("black")

    # Desenhando
    pygame.draw.circle(screen,"white", [x / 2, y / 2], 300)
    

    # Desenhando comidas
    for com in listaComida:
        com.draw()

    # Desenhando entidades
    for num, ent in enumerate(listaEnt):
        ent.draw()
        if ent.calculaDistancia(x / 2, y / 2) < 300:
            ent.randomMove()


    # Trocando o buffer para aparecer oque foi desenhado
    pygame.display.flip()

    clock.tick(60)  # Limite de FPS

pygame.quit()