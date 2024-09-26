import pygame
from constants import *
from circleshape import CircleShape
import random

class Ball(CircleShape):
    def __init__(self, x, y, radius = BALL_RADIUS, containers = ()):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1) * BALL_SPEED
        self.color = COLORS[random.randint(0,9)]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, width=2)

    def update(self, dt):
        self.velocity.y += GRAVITY
        self.position += self.velocity * dt

    def bounce(self, balls):

        if MAX_BALLS > balls:
            self.kill()
            direction_to_center = (CENTER - self.position).normalize()
            newAngle1 = random.uniform(-25, 10)
            newAngle2 = random.uniform(-25, 10)
            velo1 = direction_to_center.rotate(newAngle1) * self.velocity.length()
            velo2 = direction_to_center.rotate(newAngle2) * self.velocity.length()
            ball = Ball(self.position.x,self.position.y)
            ball.velocity = velo1
            ball2 = Ball(self.position.x,self.position.y)
            ball2.velocity = velo2
        self.position -= self.velocity.normalize() * .5
        self.velocity = -self.velocity

        print('bounce')