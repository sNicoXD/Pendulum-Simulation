import pygame,sys
import color
import math
from pendulum import Pendulum

pygame.init()
size = width, height = 1200, 1200
screen = pygame.display.set_mode(size)

graph = Pendulum(500, [600, 600], 60, 50, 1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(color.BLACK)
    graph.trace(screen)
    graph.draw(screen, width, height)
    graph.simulate()
    pygame.display.flip()
