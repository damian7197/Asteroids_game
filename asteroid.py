import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    #metodo para crear la figura del asteroide
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    #metodo para actualizar la posicion 
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        #finaliza si el asteroide es del minimo tamaño permitido
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        #genero angulo aleatorio de spliteo
        random_angle = random.uniform(20,50)
        
        vector_1 = self.velocity.rotate(random_angle)
        vector_2 = self.velocity.rotate(-random_angle)
        
        #genero los dos nuevos asteroides, ajustando su direccion y velocidad
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector_1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector_2 * 1.2
        