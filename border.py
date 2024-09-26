import pygame
from constants import *
from circleshape import CircleShape

class Border(CircleShape):
    def __init__(self, x, y, radius = BORDER_RADIUS, containers = ()):
        super().__init__(x, y, radius)
        self.size = 2
        self.size_timer = 0

    def update(self, dt):
        self.size_timer -=dt

    def draw(self, screen):
        if self.size_timer > 0: 
            self.size = 5
        else:
            self.size = 2
        pygame.draw.circle(screen, "white", self.position, self.radius, width=self.size)
