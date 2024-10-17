import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()  
    #definiendo el tamaño de la pantalla
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    #creando un objeto clock
    clock = pygame.time.Clock() 
    
    #creamos grupos de sprites para manejar objetos con caracteristicas en comun
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #Asignamos grupos a las clases, para que las instancias se manejen automaticamente
    Player.containers = (updatable, drawable)   
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    dt = 0 #delta time, por convencion
    
    while True:
        for event in pygame.event.get(): #capturo el evento para cerrar la pantalla
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable: #se actualizan todos los objetos actualizables
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
                
        
        screen.fill((0,0,0)) #los parametros son el color
        
        for obj in drawable: #se actualizan todos los objetos dibujables
            obj.draw(screen) 
        pygame.display.flip()
        
        #limitar el framerate a 60 FPS
        dt = clock.tick(60) / 1000 #ademas convierto el tiempo a segundos para manejar la actualizacion de objetos
        
    
        

if __name__ == "__main__":
    main()
