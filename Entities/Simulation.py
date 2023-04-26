import Entities.Entity as Entity
import Entities.Food as Food
import pygame
import Configuration as configuration
from math import cos,sin,radians,floor,sqrt

class Simulation:
    
    def __init__(self, entity_quantity, food_quantity, arena_radius):
        
        self.global_food = [ [[], [], [], [], []]  , [[], [], [], [], []],   [[], [], [], [], []] , [[], [], [], [], []] ]
        self.arena_radius = arena_radius
        self.entity_list = []
        self.food_list = []
        self.food_quantity = food_quantity
        self.entity_quantity = entity_quantity
        self.food_quantity_present = food_quantity
        self.entity_quantity_alive = entity_quantity
        self.show_render = False

        self.startRound(entity_quantity,food_quantity)

    def startRound(self, entity_quantity, food_quantity, restart = True):
        if restart:
            self.global_food = [ [[], [], [], [], []]  , [[], [], [], [], []],   [[], [], [], [], []] , [[], [], [], [], []] ]
            self.entity_list = []
            self.food_list = []
            self.food_quantity = food_quantity
            self.entity_quantity = entity_quantity
            self.food_quantity_present = food_quantity
            self.entity_quantity_alive = entity_quantity


        for i in range(entity_quantity):
            position_x = configuration.x / 2 + cos(radians((360 / entity_quantity) * i)) * (self.arena_radius - 2)
            position_y = configuration.y / 2 - sin(radians((360 / entity_quantity) * i)) * (self.arena_radius - 2)

            self.entity_list.append(Entity.Entity(configuration.screen, position_x,position_y, 180 + (360 / entity_quantity) * i))

        for c in range(food_quantity):
            self.food_list.append(Food.Food(configuration.screen, self.arena_radius, [configuration.screen.get_size()[0] / 2, configuration.screen.get_size()[1] / 2], "orange"))

        for food_for in self.food_list:
            food_x = food_for.getPosition()[0]
            food_y = food_for.getPosition()[1]
            center_distance = sqrt((food_x - (configuration.x / 2)) ** 2 + (food_y - (configuration.y / 2)) ** 2)
            food_circle = floor( center_distance / 60)


            if food_x > configuration.x / 2:
                if food_y < configuration.y / 2:
                    self.global_food[0][food_circle].append(food_for)
                if food_y > configuration.y / 2:
                    self.global_food[3][food_circle].append(food_for)

            if food_x < configuration.x / 2:
                if food_y < configuration.y / 2:
                    self.global_food[1][food_circle].append(food_for)
                if food_y > configuration.y / 2:
                    self.global_food[2][food_circle].append(food_for)
        
        

        self.drawArena()
        self.drawFoods()
        self.drawEntities()

        pygame.display.flip()

    def drawArena(self):
        pygame.draw.circle(configuration.screen, "white", [configuration.x / 2, configuration.y / 2], self.arena_radius)

    def drawFoods(self):
        for food in self.food_list:
            if not food.devoured:
                food.draw()
            
    def drawEntities(self):
        for entity in self.entity_list:
            entity.draw()

    def drawHemispheres(self):
        pygame.draw.line(configuration.screen, "red", [0, configuration.y / 2], [configuration.x, configuration.y / 2])
        pygame.draw.line(configuration.screen, "red", [configuration.x / 2, 0], [configuration.x / 2, configuration.y])

    def drawCircles(self):
        for i in range(5, 0, -1):
            color = 255 - (255 / 6) * i
            radius = (self.arena_radius / 5) * i
            pygame.draw.circle(configuration.screen, [color, color, color], [configuration.x / 2, configuration.y / 2], radius)

    def tick(self, colision = True):
        for entity in self.entity_list:
            entity.draw()
            
            if entity.alive:
                if entity.distanceBetween(configuration.x / 2, configuration.y / 2) < self.arena_radius - 1:
                    entity.move()
                    if colision:
                        self.colision(entity)                
                else:
                    entity.alive = False
                    self.entity_quantity_alive -= 1

    def colision(self, entity):
        ent_x = entity.getPosition()[0]
        ent_y = entity.getPosition()[1]

        center_distance = sqrt((ent_x - (configuration.x / 2)) ** 2 + (ent_y - (configuration.y / 2)) ** 2)
        ent_circle = floor(center_distance / 60)

        if ent_x > configuration.x / 2:
            if ent_y < configuration.y / 2:
                ent_hemisphere = 0
            else:
                ent_hemisphere = 3

        else:
            if ent_y < configuration.y / 2:
                ent_hemisphere = 1
            else:
                ent_hemisphere = 2
        
        for food_for in self.global_food[ent_hemisphere][ent_circle]:
            if not food_for.devoured:
                food_x = food_for.position_x
                food_y = food_for.position_y
                radius_sum = configuration.entity_radius + configuration.food_radius

                if entity.distanceBetween(food_x, food_y) <= radius_sum:
                    food_for.devoured = True
                    self.food_quantity_present -= 1
                if self.show_render:
                    pygame.draw.line(configuration.screen, "blue", [ent_x, ent_y], [food_x, food_y])

    def drawStatistics(self, position):        
        font = pygame.font.SysFont("Verdana", 20)
        text_entities = font.render(f'entidades vivas: {str(self.entity_quantity_alive)}',True, "white")
        text_food = font.render(f'comidas presentes: {str(self.food_quantity_present)}',True, "white")

        configuration.screen.blit(text_entities, position)
        configuration.screen.blit(text_food, [position[0], position[1] + 25])

    def drawRender(self):
        self.show_render = not self.show_render