import pygame
import color, misc
import math
class Pendulum:
    length = 0
    origin = [0, 0]
    angle = 0
    mass = 50
    deltaT = 0
    iV = 0
    posRec = []


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
        self.posRec.append([px, py])
        if len(self.posRec) == 50:
            self.posRec.remove(self.posRec[0])

    def set_angle(self, angle):
        self.angle = angle
    
    def simulate(self):
        a = -9.81 / self.length * math.sin(math.radians(self.angle))
        o2 = self.iV + a * self.deltaT
        angle2 = self.angle + self.iV * self.deltaT
        self.iV = o2
        self.angle = angle2
        print(self.angle)

    def trace(self, screen):
        for n in range(0, len(self.posRec) - 1):
            pygame.draw.line(screen, [0, misc.sloping(50, 255, 50, n), 0], self.posRec[n], self.posRec[n + 1], 2)
