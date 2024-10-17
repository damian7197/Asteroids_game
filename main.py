import pygame
from constants import *
from player import Player

def main():
    pygame.init()  
    #definiendo el tamaño de la pantalla
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    #creando un objeto clock
    clock = pygame.time.Clock() 
    
    udpatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (udpatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    dt = 0 #delta time, por convencion
    
    while True:
        for event in pygame.event.get(): #capturo el evento para cerrar la pantalla
            if event.type == pygame.QUIT:
                return
            
        for obj in udpatable:
            obj.update(dt)
        
        screen.fill((0,0,0)) #los parametros son el color
        
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        #limitar el framerate a 60 FPS
        dt = clock.tick(60) / 1000
        
    
        

if __name__ == "__main__":
    main()
