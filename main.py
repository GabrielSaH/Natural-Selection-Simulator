import Classes.entidade as entidade
import Funcoes.pygameHelpers as pygameHelpers
import Classes.food as food
import Classes.simulacao as simulacao
import Variaveis.variaveis as variaveis

import pygame

from math import sin,cos,tan,radians, pi, sqrt


simu = simulacao.simulacao(40, 50, 300)


# Condicional Loop
running = True

# Ciclo do jogo
while running:
    pygameHelpers.pause(variaveis.screen)


    # Checa a stack de eventos
    # pygame.QUIT é o evento de clicar no X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Configurando pause
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygameHelpers.pause(variaveis.screen)         

    # apaga o ultimo frame enxendo a tela de preto
    variaveis.screen.fill("black")

    # Desenha Arena
    simu.desenhaArena()    
    
    simu.DrawCircolos()


    # Desenha Comida 
    simu.desenhaComida()
            
    # Desenha Entidades e Calcula Colisoes
    
    #   Simu.tick()
        #   Desenha Entidades

        #   Move Entidades

            #   Devora comida
    
    simu.tick()
    
    # for num, ent in enumerate(listEnt):
        
        # # Todas entidades são desenhadas
        # ent.draw()
        
        # # Caso a entidade nao tenha saido da arena, ou seja, ainda ta na simulaçao
        # if ent.calculaDistancia(variaveis.x / 2, variaveis.y / 2) < 300:
            
        #     ent.randomMove()

        #     # lista contendo = [posicaoX, posicaoY, Raio]            
        #     posicaoEntidade = ent.getCurrentPosition()
            

        #     # Percorre as comidas
        #     for currentFood in listFood:

        #         # Se ainda nao foi devorada
        #         if not currentFood.devorada:

        #             # lista contendo = [posicaoX, posicaoY, Raio]            
        #             posicaoComida = currentFood.getPosition()

        #             # Calcula a distancia entre entidade e comida atual
        #             distance = ent.calculaDistancia(posicaoComida[0], posicaoComida[1])
                
        #             # distancia max igual soma dos raios
        #             distanciaMAX = posicaoComida[2] + posicaoEntidade[2]

        #         if distance <= distanciaMAX:

        #             #muda para devorada, ou seja, nao sera mais desenhada e nem calculada
        #             currentFood.devorada = True


    simu.DrawEmisferios()
    # Trocando o buffer para aparecer oque foi desenhado
    pygame.display.flip()

    variaveis.clock.tick(60)  # Limite de FPS

pygame.quit()