import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable) # type: ignore
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000
        updateable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        
    
    
if __name__ == "__main__":
    main()