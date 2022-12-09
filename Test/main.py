import pygame,sys
import color
import math
from pendulum import Pendulum

pygame.init()
size = width, height = 1200, 1200
screen = pygame.display.set_mode(size)

graph = Pendulum(300, 300, [600, 600], 10, 90, 500, 50, 0.001)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(color.BLACK)
    graph.draw(screen, width)
    graph.physicSim1()
    graph.physicSim2()
    graph.trace(screen)
    pygame.display.flip()
