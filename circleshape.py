import pygame

# Clase base para objetos del juego
class CircleShape(pygame.sprite.Sprite): 
    def __init__(self, x, y, radius): 
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__() #inicializando contructor mediante herencia

        self.position = pygame.Vector2(x, y) #extendemos la clase sprite con:
        self.velocity = pygame.Vector2(0, 0) # Posicion, velocidad y radio
        self.radius = radius

    def draw(self, screen):
        # Sub clases deben sobreescribirlo
        pass

    def update(self, dt):
        # sub clases deben sobreescribirlo
        pass
    
    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius