import pygame
import color, misc
import math
class Pendulum:
    length1 = 0
    length2 = 0
    origin = [0, 0]
    angle1 = 0
    angle2 = 0
    mass1 = 50
    mass2 = 50
    deltaT = 0
    iV = 0
    g = -9.81
    posRec = []
    posRec2 = []

    def __init__(self, length1, length2, origin, initAngle1, initAngle2, mass1, mass2, deltaT):
        self.length1 = length1
        self.length2 = length2
        self.origin = origin
        self.angle1 = initAngle1
        self.angle2 = initAngle2
        self.mass1 = mass1
        self.mass2 = mass2
        self.deltaT = deltaT
    

    def draw(self, screen, width):
        ox = width / 2
        oy = 0
        px = self.length1 * math.sin(math.radians(self.angle1)) + ox
        py = self.length1 * math.cos(math.radians(self.angle1)) + oy
        pygame.draw.line(screen, color.WHITE, (ox, oy), (px, py), 2)
        pygame.draw.circle(screen, color.WHITE, (px, py), 40)
        self.posRec.append([px, py])
        if len(self.posRec) == 50:
            self.posRec.remove(self.posRec[0])

        ax = self.length2 * math.sin(math.radians(self.angle2)) + px
        ay = self.length2 * math.cos(math.radians(self.angle2)) + py
        pygame.draw.line(screen, color.WHITE, (px, py), (ax, ay), 2)
        pygame.draw.circle(screen, color.WHITE, (ax, ay), 40)
        self.posRec2.append([ax, ay])
        if len(self.posRec2) == 50:
            self.posRec2.remove(self.posRec2[0])

    def set_angle(self, angle1):
        self.angle1 = angle1
    
    def physicSim1(self):
        a = -9.81 / self.length1 * math.sin(math.radians(self.angle1))
        o2 = self.iV + a * self.deltaT
        angle1_2 = self.angle1 + self.iV * self.deltaT
        self.iV = o2
        self.angle1 = angle1_2
        
    def physicSim2(self):
        a = -9.81 / self.length2 * math.sin(math.radians(self.angle2))
        o2 = self.iV + a * self.deltaT
        angle2_2 = self.angle2 + self.iV * self.deltaT
        self.iV = o2
        self.angle2 = angle2_2
        print(self.angle2)

    def trace(self, screen):
            for n in range(0, len(self.posRec) - 1):
                pygame.draw.line(screen, [0, misc.sloping(50, 255, 50, n), 0], self.posRec[n], self.posRec[n + 1], 2)
            for n in range(0, len(self.posRec2) - 1):
                pygame.draw.line(screen, [0, misc.sloping(50, 255, 50, n), 0], self.posRec2[n], self.posRec2[n + 1], 2)




