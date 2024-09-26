import pygame
from constants import *
from circleshape import CircleShape
from border import Border
from ball import Ball

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()

# Load the music file
pygame.mixer.music.load('pop.mp3')

# Set the volume (optional)
pygame.mixer.music.set_volume(0.5)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    updatableGroup = pygame.sprite.Group()
    drawableGroup = pygame.sprite.Group()
    borderGroup = pygame.sprite.Group()
    ballGroup = pygame.sprite.Group()

    Border.containers = (borderGroup, drawableGroup, updatableGroup)
    Ball.containers = (ballGroup, drawableGroup, updatableGroup)


    border = Border(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    music_pos = 1
    music_timer = 0
    balls = 1
    while(True):
        screen.fill('Black')        
        for item in updatableGroup:
            item.update(dt)
        for item in drawableGroup:
            item.draw(screen)
        for item in borderGroup:
            for ball in ballGroup:
                if ball.collisions(item):
                    pygame.mixer.music.stop()
                    item.size_timer = .05
                    ball.bounce(balls)
                    balls += 1
                    pygame.mixer.music.play(start=0.17)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000
        print(dt)
        pygame.display.flip()#dont ever forget

main()