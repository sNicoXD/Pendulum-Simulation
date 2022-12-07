import pygame, color1, math
class Pendulum:
    length = 0
    origin = [0, 0]
    angle = 0
    mass = 50

    def __init__(self, length, origin, init_angle, mass):
        self.length = length
        self.origin = origin
        self.angle = init_angle
        self.mass = mass

    def draw(self, screen, width, height):
        pygame.draw.line(screen, color1.WHITE, (width / 2, height / 2), (width / 2, 0), 2)
        pygame.draw.circle(screen, color1.WHITE, (width / 2, height / 2), self.mass)
   
    def endpoint(self, origin, length):

    def physics(self, mass):
        force_g = mass * 9.
        force_t = force_g 
        period = 2 * math.pi * math.sqrt(length / 9.80665)


