import sys
import pygame
from asteroid import Asteroid
from asteroidfield import *
from constants import *
from player import Player, Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable) # type: ignore
    
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable) # type: ignore
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable) # type: ignore
    AsteroidField.containers = (updateable) # type: ignore
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)    
    asteroidfield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            
        screen.fill("black")
        dt = clock.tick(60) / 1000
        
        updateable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision_detection(player):
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision_detection(bullet):
                    asteroid.split()
                    bullet.kill()    
                
        for thing in drawable:
            thing.draw(screen)
            
            
            
        pygame.display.flip()
        
    
    
if __name__ == "__main__":
    main()