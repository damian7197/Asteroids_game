from circleshape import CircleShape
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self ,x ,y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
   
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        #Creo un vector que apunte hacia arriba y uso un metodo de rotacion
        forward = pygame.Vector2(0, 1).rotate(self.rotation) 
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 #uso esto para ajustar el tamaño del lateral
        #Calculo los tres vertices de mi tringulo
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        #Retorno una lista con los tres vertices juntos
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
    
    
        
        