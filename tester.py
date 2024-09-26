import pygame
import random
from pygame.math import Vector2

# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()

# Load the music file
pygame.mixer.music.load('slowboy_astro.mp3')

# Set the volume (optional)
pygame.mixer.music.set_volume(0.5)

# Define constants
CENTER = Vector2(400, 300)
BALL_RADIUS = 20
GRAVITY = 0.5

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius=BALL_RADIUS):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.position = Vector2(x, y)
        self.velocity = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
        self.gravity = GRAVITY

    def update(self, dt):
        self.velocity.y += self.gravity
        self.position += self.velocity * dt
        self.rect.center = self.position

    def bounce(self):
        self.kill()
        direction_to_center = (CENTER - self.position).normalize()
        newAngle1 = random.uniform(-10, 10)
        newAngle2 = random.uniform(-10, 10)
        bounce_speed = 5  # Set a constant bounce speed
        velo1 = direction_to_center.rotate(newAngle1) * bounce_speed
        velo2 = direction_to_center.rotate(newAngle2) * bounce_speed
        ball1 = Ball(self.position.x, self.position.y)
        ball1.velocity = velo1
        ball1.gravity = -self.gravity
        ball2 = Ball(self.position.x, self.position.y)
        ball2.velocity = velo2
        ball2.gravity = -self.gravity

        # Increment the song position by 2 seconds
        current_pos = pygame.mixer.music.get_pos() / 1000.0
        new_pos = current_pos + 2
        pygame.mixer.music.play(start=new_pos)

        print('bounce')
        return ball1, ball2

# Initialize Pygame screen
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create a ball
ball = Ball(400, 300)
all_sprites = pygame.sprite.Group()
all_sprites.add(ball)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update(1 / 60)

    # Check for collision and bounce
    if ball.rect.left <= 0 or ball.rect.right >= 800 or ball.rect.top <= 0 or ball.rect.bottom >= 600:
        ball1, ball2 = ball.bounce()
        all_sprites.add(ball1, ball2)

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw all sprites
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
