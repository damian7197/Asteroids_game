import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y,velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
        # Eliminar la bala si está fuera de los límites de la pantalla
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()  # Método de pygame.sprite.Sprite para eliminar el sprite del grupo
    
  
        