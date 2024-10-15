import pygame
from constants import *

def main():
    pygame.init()  
    #definiendo el tamaño de la pantalla
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    
    #creando un objeto clock
    clock = pygame.time.Clock() 
    dt = 0 #delta time, por convencion
    
    while True:
        for event in pygame.event.get(): #capturo el evento para cerrar la pantalla
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0)) #los parametros son el color
        pygame.display.flip()
        #limitar el framerate a 60 FPS
        dt = clock.tick(60) / 1000
        
    
        

if __name__ == "__main__":
    main()
