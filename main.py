import pygame,sys
import color
from pendulum import Pendulum

pygame.init()
size = width, height = 1200, 1200
screen = pygame.display.set_mode(size)

graph = Pendulum(600, [600, 600], 30, 50)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(color.BLACK)
    graph.draw(screen, width, height)
    pygame.display.flip()
