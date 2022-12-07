import pygame, color
import math
class Pendulum:
    length = 0
    origin = [0, 0]
    angle = 0
    mass = 50
    deltaT = 0
    iV = 0

    def __init__(self, length, origin, init_angle, mass, deltaT):
        self.length = length
        self.origin = origin
        self.angle = init_angle
        self.mass = mass
        self.deltaT = deltaT
    

    def draw(self, screen, width, height):
        ox = width / 2
        oy = 0
        px = self.length * math.sin(math.radians(self.angle)) + ox
        py = self.length * math.cos(math.radians(self.angle)) + oy
        pygame.draw.line(screen, color.PURPLE, (ox, oy), (px, py), 2)
        pygame.draw.circle(screen, color.BLUE, (px, py), self.mass)

    def set_angle(self, angle):
        self.angle = angle
    
    def simulate(self):
        a = -9.81 / self.length * math.sin(math.radians(self.angle))
        o2 = self.iV + a * self.deltaT
        angle2 = self.angle + self.iV * self.deltaT
        self.iV = o2
        self.angle = angle2
        print(self.angle)
#

#x l*sin + width/2
#y l*con
# width/2, 0