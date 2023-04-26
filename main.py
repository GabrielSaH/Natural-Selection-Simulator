import Helpers.PyGameHelper as PyGameHelper
import Entities.Simulation as Simulation
import Entities.fps as fps
import Configuration as configuration
import pygame

simulation = Simulation.Simulation(10, 30, 300)

running = True

frame_second = fps.fps([20,20])

fps_limit = 60

show_render_division = False

while running:
    #PyGameHelper.pause(configuration.screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                PyGameHelper.pause(configuration.screen)         

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_RIGHT:
                fps_limit = fps_limit * 1.5

            if event.key == pygame.K_LEFT:
                fps_limit = fps_limit / 1.5

            if event.key == pygame.K_UP:
                simulation.drawRender()

            if event.key == pygame.K_DOWN:
                show_render_division = not show_render_division

            if event.key == pygame.K_r:
                simulation.startRound(10,30)
    
    configuration.screen.fill("black")

    simulation.drawArena()    
    
    if show_render_division: simulation.drawCircles()

    simulation.drawFoods()

    simulation.tick()

    if show_render_division: simulation.drawHemispheres()

    simulation.drawStatistics([20,45])

    frame_second.draw()

    pygame.display.flip()

    configuration.clock.tick(fps_limit) # Limitador de fps
    
pygame.quit()