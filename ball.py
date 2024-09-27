import pygame
from constants import *
from circleshape import CircleShape
import random

pygame.mixer.init()
pygame.mixer.music.load('pop.mp3')
pygame.mixer.music.set_volume(0.5)

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
        self.pop_effect()
        if MAX_BALLS > balls:
            self.kill()
            direction_to_center = (CENTER - self.position).normalize()
            for i in range(NEW_BALLS):
                self.spawn_center()
        self.color = COLORS[random.randint(0,9)]
        self.position -= self.velocity.normalize() * .5
        self.velocity = -self.velocity

    def spawn_at_position(self):
        direction_to_center = (CENTER - self.position).normalize()
        newAngle = random.uniform(-25, 10)
        velo = direction_to_center.rotate(newAngle) * self.velocity.length()
        ball = Ball(self.position.x,self.position.y)
        ball.velocity = velo

    def spawn_center(self):
        ball = Ball(CENTER[0], CENTER[1])
        newAngle = random.uniform(-50, 50)
        ball.velocity = - ball.velocity.rotate(newAngle)

    def pop_effect(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.play(start=0.15)