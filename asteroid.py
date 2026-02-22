import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        # The angle for used for splitting the asteroids
        new_random_angle = random.uniform(20, 50)
        new_asteroid_1_velocity = self.velocity.rotate(new_random_angle)
        new_asteroid_2_velocity = self.velocity.rotate(-new_random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid_1.velocity += new_asteroid_1_velocity * 1.2

        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid_2.velocity += new_asteroid_2_velocity * 1.2
