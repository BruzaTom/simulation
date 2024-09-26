import pygame
import math
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collisions(self, CircleShape):
        dx = self.position.x - CENTER[0]
        dy = self.position.y - CENTER[1]
        distance = math.sqrt(dx**2 + dy**2)
        if distance + self.radius >= BORDER_RADIUS:
            return True
        return False