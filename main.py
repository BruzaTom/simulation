import pygame
from constants import *
from circleshape import CircleShape
from border import Border

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    updatableGroup = pygame.sprite.Group()
    drawableGroup = pygame.sprite.Group()
    Border.containers = (drawableGroup)

    border = Border(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 10)

    while(True):
        screen.fill('Black')        
        for item in updatableGroup:
            item.update(dt)
        for item in drawableGroup:
            item.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000
        print(dt)
        pygame.display.flip()#dont ever forget

main()