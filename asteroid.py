import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= (ASTEROID_MIN_RADIUS):
            return

        rand_angle = random.uniform(20, 50)
        velo1 = self.velocity.rotate(rand_angle) * 1.2
        velo2 = self.velocity.rotate(-rand_angle) * 1.2

        new_rad = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_rad)
        new_asteroid1.velocity = velo1
    
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_rad)
        new_asteroid2.velocity = velo2

