import pygame,sys,color
pygame.init()


size = width, height = 800, 800
screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(color.RED)
    pygame.display.flip()
    