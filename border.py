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
        self.grow_radius = radius

    def update(self, dt):
        self.timer -= dt
        if self.timer > 0:
            if self.radius <= MAX_RADIUS:
                self.radius += .5
        else:
            if self.radius > BORDER_RADIUS:
                self.radius -= .5 * 3

    def draw(self, screen):
        if self.timer > 0:
            pygame.draw.circle(screen, self.bordercolor, self.position, self.radius, width=self.width)
        else: 
            pygame.draw.circle(screen, self.bordercolor, self.position, self.radius, width=self.width)

    def effect(self):
        self.bordercolor = COLORS[random.randint(0,len(COLORS)-1)]
        #self.bordercolor = COLORS[6]
            
        
