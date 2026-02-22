import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # Values to spawn in middle of screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Group definition
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # TODO - not needed since using group
        # player.update(dt)
        updatable.update(dt)

        # Detect if asteroids collided with player
        for asteroid_item in asteroids:
            if asteroid_item.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot_item in shots:
                if shot_item.collides_with(asteroid_item):
                    log_event("asteroid_shot")
                    asteroid_item.split()
                    shot_item.kill()

        # Paints the canvas black
        screen.fill("black")

        # TODO - not needed since using group
        # player.draw(screen)

        # Draws the items
        for drawable_item in drawable:
            drawable_item.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
