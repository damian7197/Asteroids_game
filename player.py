from circleshape import CircleShape
from constants import *
import pygame
from shot import Shot

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
        self.rotation += PLAYER_TURN_SPEED * dt #Ajusto la rotacion en tiempo real
    
    def update(self, dt): #metodo que define como se comportan las teclas de movimiento
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt): #definimos el movimiento hacia atras y adelante
        forward = pygame.Vector2(0, 1).rotate(self.rotation) #creamos un vector, lo rotamos 
        self.position += forward * PLAYER_SPEED * dt #calculamos su largo y lo agregamos a la posicion actual
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEDD
        
    
    
        
        