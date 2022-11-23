import pygame, color
class Pendulum:
    length = 0
    origin = [0, 0]
    angle = 0
    mass = 500

    def __init__(self, length, origin, init_angle, mass):
        self.length = length
        self.origin = origin
        self.angle = init_angle
        self.mass = mass

    def draw(self, screen, width, height):
        pygame.draw.line(screen, color.RED, (width / 2, height / 2), (width / 2, 0), 2)
        pygame.draw.circle(screen, color.BLUE, (width / 2, height / 2), self.mass)



