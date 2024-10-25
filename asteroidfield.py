import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    #Lista de cuatro listas, donde cada una representa un borde donde puedo generar asteroides
    #El primer valor define la direccion en la que se generara
    #El segundo valor calcula la posicion en el borde correspondiente
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT), #se asegura que se genere fuera de panatlla y forma aleatoria
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius, velocity) 
        return asteroid #creo un asteroide y le doy su velocidad
    
    def update(self, dt):
        #Contador para manejar el tiempo de spawn de los asteroides
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE: 
            self.spawn_timer = 0

            #Spawneo un nuevo asteoide en un eje al azar
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed#uso el vector del eje seleccionado y le doy su velocidad
            velocity = velocity.rotate(random.randint(-30, 30)) #altero un poco la direccion del vector -> (asteroide)
            position = edge[1](random.uniform(0, 1)) #Genero un valor entre 0 y 1 para lambda
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)