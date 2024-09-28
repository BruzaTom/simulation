import pygame
from constants import *
from circleshape import CircleShape
import random

class Border(CircleShape):
    def __init__(self, x, y, radius = BORDER_RADIUS, containers = ()):
        super().__init__(x, y, radius)
        self.width = 2
        self.timer = 0
        self.bordercolor = 'white'

    def update(self, dt):
        self.timer -=dt

    def draw(self, screen):
        if self.timer > 0:
            pygame.draw.circle(screen, self.bordercolor, self.position, self.radius, width=self.width)

    def effect(self):
        #self.bordercolor = COLORS[random.randint(0,len(COLORS)-1)]
        self.bordercolor = COLORS[6]
            
        
