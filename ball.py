import pygame
from constants import *
from circleshape import CircleShape
import random
import math

class Ball(CircleShape):
    def __init__(self, x, y, radius = BALL_RADIUS, containers = ()):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1) * BALL_SPEED
        self.color = COLORS[random.randint(0,len(COLORS)-1)]
        self.music_timer = 0
        self.music_pos = 0
        self.gravity = GRAVITY
        self.width = self.radius
        self.timer = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, width=self.width)

    def update(self, dt):
        if self.timer > 0:
            self.width = 2
            self.timer -= dt
        else:
            self.width = self.radius
        self.music_timer -= dt
        self.velocity.y += self.gravity
        self.position += self.velocity * dt

    def bounce(self, balls):
        #self.pop_effect()
        if MAX_BALLS > balls:
            self.split()
        else:
            self.gravity = 1
            self.keep_bouncing()

    def collisions2(self, Ball):
        dx = self.position.x - Ball.position.x
        dy = self.position.y - Ball.position.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance <= self.radius + Ball.radius:
            return True
        return False

    def split(self):
        self.kill()
        for i in range(NEW_BALLS):
            self.spawn_center()

    def keep_bouncing(self):
        self.safty()
        #self.color = COLORS[random.randint(0,len(COLORS)-1)]
        direction_to_center = (CENTER - self.position).normalize()
        newAngle = random.uniform(-25, 25)
        velo = direction_to_center.rotate(newAngle) * self.velocity.length()
        self.velocity = velo
        
    def to_bottom(self):
        direction_to_bottom = ((CENTER[0], CENTER[1] + BORDER_RADIUS) - self.position).normalize()
        newAngle = random.uniform(-25, 10)
        self.position -= self.velocity.normalize() * .5
        self.velocity = direction_to_bottom.rotate(newAngle) * self.velocity.length()

    def spawn_at_position(self):
        direction_to_center = (CENTER - self.position).normalize()
        newAngle = random.uniform(-25, 25)
        velo = direction_to_center.rotate(newAngle) * self.velocity.length()
        self.safty()#protects from sticking
        ball = Ball(self.position.x,self.position.y, radius=random.randint(8,20))
        ball.timer = 0.5
        ball.color = COLORS[random.randint(0,len(COLORS)-1)]
        ball.velocity = velo

    def safty(self):
        if self.position.x < CENTER[0]:
            self.position.x += 2
        if self.position.x > CENTER[0]:
            self.position.x -= 2
        if self.position.y < CENTER[1]:
            self.position.y += 2
        if self.position.y > CENTER[1]:
            self.position.y -= 2

    def spawn_center(self):
        ball = Ball(CENTER[0], CENTER[1], radius=random.randint(3,20))
        ball.timer = 0.5
        newAngle = random.uniform(-120, 120)
        ball.velocity = - ball.velocity.rotate(newAngle)

    def pop_effect(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('sounds/pop_edit.mp3')
        pygame.mixer.music.set_volume(0.5)
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        pygame.mixer.music.play(start=0.12)