import pygame
from constants import *
from circleshape import CircleShape
from border import Border
from ball import Ball
import random

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('7weeks3days_tiktok.mp3')
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
    
    music_pos = 1.15
    music_timer = 0
    balls = 1
    while(True):

        if music_timer > 0:
            music_pos += dt
            music_timer -= dt
        else:
            pygame.mixer.music.stop()
        screen.fill('Black')        
        for item in updatableGroup:
            item.update(dt)
        for item in drawableGroup:
            item.draw(screen)
        for item in borderGroup:
            for ball in ballGroup:
                if ball.collisions(item):
                    music_timer = dt * 10
                    item.timer = .5
                    item.effect()
                    ball.bounce(balls)
                    balls += 1
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.play(start=music_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000
        #print(dt)
        pygame.display.flip()#dont ever forget

main()