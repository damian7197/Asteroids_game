import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from usuarios import guardar_high_score
import json
from high_scores import actualizar_high_scores
from save_game import show_pause_menu, load_game_state

def game(nombre_usuario):
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
    
    load = input("¿Quieres continuar tu última partida? (S/n): ") or "s"
    game_state = None
    if load.lower() == "s":
        game_state = load_game_state()
    if game_state:
        # Restaurar el estado del jugador
        asteroidfield = AsteroidField()
        dt = 0
        player = Player(game_state["player"]["x"], game_state["player"]["y"])

        # Restaurar asteroides
        for ast in game_state["asteroids"]:
            asteroid = asteroidfield.spawn(ast["radius"],pygame.Vector2(ast["x"], ast["y"]),pygame.Vector2(ast["velocity"]["x"],ast["velocity"]["y"]))
            asteroids.add(asteroid)

        # Restaurar balas
        for shot_data in game_state["shots"]:
            x, y = shot_data["x"], shot_data["y"]
            if 0 <= x <= SCREEN_WIDTH and 0 <= y <= SCREEN_HEIGHT:
                shot = Shot(x, y, pygame.Vector2(shot_data["velocity"]["x"], shot_data["velocity"]["y"]))
                shots.add(shot)
                print(f"Shot loaded at position ({x}, {y}) with velocity {shot_data['velocity']}")
            else:
                print(f"Shot at position ({x}, {y}) skipped as it's outside screen bounds.")
           
            #shot = Shot(shot_data["x"], shot_data["y"],pygame.Vector2(shot_data["velocity"]["x"], shot_data["velocity"]["y"]))
            #shots.add(shot)
            
            
        
        score = game_state["score"]
 
    else:
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        score = 0
        asteroidfield = AsteroidField()
        dt = 0 #delta time, por convencion
    
    font = pygame.font.Font(None, 36)  # fuente para la puntuacion
    high_score = 0
    
    with open('./usuarios.json', 'r') as f:
        usuarios = json.load(f)
        high_score = usuarios[nombre_usuario]['high_score'] 
    
    while True:
        for event in pygame.event.get(): #capturo el evento para cerrar la pantalla
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pausar el juego
                    show_pause_menu(player, asteroids, shots, score, screen, clock)
            
        for obj in updatable: #se actualizan todos los objetos actualizables
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                guardar_high_score(nombre_usuario, score)
                actualizar_high_scores(nombre_usuario,score,"./high_scores.csv")
                sys.exit()
        
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()      #bucle para detectar las colisiones de asteroide con disparos  
                    asteroid.split()
                    if asteroid.radius > 40:
                        score += 5
                    elif asteroid.radius > 25:
                        score += 10
                    else:
                        score += 15
          
        screen.fill((0,0,0)) #los parametros son el color
        
        for obj in drawable: #se actualizan todos los objetos dibujables
            obj.draw(screen)
        
        # Dibujar la puntuación en pantalla en la esquina superior izquierda
        score_text = font.render(f"Puntuación: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10)) 
        
        pygame.display.flip()
        
        #limitar el framerate a 60 FPS
        dt = clock.tick(60) / 1000 #ademas convierto el tiempo a segundos para manejar la actualizacion de objetos
        
    
         


  
