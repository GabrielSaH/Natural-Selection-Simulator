import Classes.entidade as entidade
import Funcoes.pygameHelpers as pygameHelpers
import Classes.food as food
import pygame
import Variaveis.variaveis as variaveis

from math import cos,sin,radians, sqrt

class simulacao:
    def __init__(self,qntEntiInicial, qntComidaInicial, raioArena):
        
        #   Atributos
        
        self.raioArena = raioArena
        
        #   Entidades
        #       Criando Variaveis de entidades
        self.listEnt = []
        
        self.listFood = []
        
        #       Populando as listas de entidades com qualquer coisa (importante para proxima funcao)
        for _ in range(qntEntiInicial):
            self.listEnt.append(1)
        
        for _ in range(qntComidaInicial):
            self.listFood.append(1)
             
        #       posicionando entidades

        self.desenhaInicioRound()

    def desenhaInicioRound(self):
        listEntNova = []
        qntEnti = len(self.listEnt)
        for i in range(qntEnti):
            
            #Calculo para colocar as entidades em volta da arena, 299 pois elas nao podem nascer com a metade delas para fora da arena
            posX = variaveis.x / 2 + cos(radians((360 / qntEnti) * i)) * (self.raioArena - 1)
            posY = variaveis.y / 2 - sin(radians((360 / qntEnti) * i)) * (self.raioArena - 1)

            listEntNova.append(entidade.entidade(variaveis.screen,posX,posY, 180 + (360 / len(self.listEnt)) * i))
        
        self.listEnt = listEntNova

        listComidaNova = []
        for c in range(len(self.listFood)):
            listComidaNova.append(food.Food(variaveis.screen, self.raioArena, [variaveis.screen.get_size()[0] / 2, variaveis.screen.get_size()[1] / 2]))
        
        self.listFood = listComidaNova

        self.desenhaArena()
        self.desenhaComida()
        self.desenhaEntidade()

        pygame.display.flip()

    def desenhaArena(self):
        pygame.draw.circle(variaveis.screen, "white", [variaveis.x / 2, variaveis.y / 2], self.raioArena)

    def desenhaComida(self):
        for com in self.listFood:
            if not com.devorada:
                com.draw()
            
    def desenhaEntidade(self):
        for ent in self.listEnt:
            ent.draw()

    def DrawEmisferios(self):
        pygame.draw.line(variaveis.screen, "red", [0, variaveis.y / 2], [variaveis.x, variaveis.y / 2])
        pygame.draw.line(variaveis.screen, "red", [variaveis.x / 2, 0], [variaveis.x / 2, variaveis.y])

    def DrawCircolos(self):
        for i in range(5, 0, -1):
            cor = 255 - (255 / 6) * i
            raio = (self.raioArena / 5) * i
            pygame.draw.circle(variaveis.screen, [cor, cor, cor], [variaveis.x / 2, variaveis.y / 2], raio)

    def tick(self):
        for ent in self.listEnt:
            ent.draw()

            if ent.viva and ent.calculaDistancia(variaveis.x / 2, variaveis.y / 2) < self.raioArena:
                ent.randomMove()
            else:
                ent.viva = False
  #   Simu.tick()
        #   Desenha Entidades

        #   Move Entidades

            #   Devora comida
    