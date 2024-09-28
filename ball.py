import pygame
from constants import *
from circleshape import CircleShape
import random


class Ball(CircleShape):
    def __init__(self, x, y, radius = BALL_RADIUS, containers = ()):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1) * BALL_SPEED
        self.color = COLORS[random.randint(0,9)]
        self.music_timer = 0
        self.music_pos = 0
        self.gravity = GRAVITY

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, width=10)

    def update(self, dt):
        self.music_timer -= dt
        self.velocity.y += self.gravity
        self.position += self.velocity * dt

    def bounce(self, balls):
        self.pop_effect()
        if MAX_BALLS > balls:
            self.kill()
            for i in range(NEW_BALLS):
                self.spawn_center()
        else:
            self.keep_bouncing()

    def keep_bouncing(self):
        self.color = COLORS[random.randint(0,9)]
        self.position -= self.velocity.normalize() * .5
        self.velocity = -self.velocity
        
    def to_bottom(self):
        direction_to_bottom = ((CENTER[0], CENTER[1] + BORDER_RADIUS) - self.position).normalize()
        newAngle = random.uniform(-25, 10)
        self.position -= self.velocity.normalize() * .5
        self.velocity = direction_to_bottom.rotate(newAngle) * self.velocity.length()

    def spawn_at_position(self):
        direction_to_center = (CENTER - self.position).normalize()
        newAngle = random.uniform(-25, 10)
        velo = direction_to_center.rotate(newAngle) * self.velocity.length()
        ball = Ball(self.position.x,self.position.y)
        ball.color = COLORS[random.randint(0,9)]
        ball.velocity = velo

    def spawn_center(self):
        ball = Ball(CENTER[0], CENTER[1])
        newAngle = random.uniform(-180, 180)
        ball.velocity = - ball.velocity.rotate(newAngle)

    def pop_effect(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('pop.mp3')
        pygame.mixer.music.set_volume(0.5)
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        pygame.mixer.music.play(start=0.12)