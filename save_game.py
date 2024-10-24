import json
import pygame
import sys
from game_logic import *
from constants import *

def save_actual_game(player, asteroids,shots,score,filename="./savegame.json"):
    #generamos un pantallaso de todos los elementos en pantalla
    game_state = {
        "player": {
            "x" : player.position.x,
            "y" : player.position.y
        },
        "asteroids" : [
            {"x": asteroid.position.x, "y": asteroid.position.y, "radius" : asteroid.radius}
            for asteroid in asteroids
        ],
        "shots" : [
            {"x" : shot.position.x, "y" : shot.position.y}
            for shot in shots
        ],
        "score": score 
    }
    
    #guardamos en el archivo el pantallaso
    with open(filename, 'w') as file:
        json.dump(game_state, file)
    print("Juego guardado exitosamente.")

def load_game_state(filename="./savegame.json"):
    try:
        with open(filename, 'r') as file:
            estado_juego = json.load(file)
        
        return estado_juego
    except FileNotFoundError:
        print("No hay una partida guardada.")
        return None

def show_pause_menu(player, asteroids, shots, score,screen,clock):
    #manejo de todas las opciones del menu pausado, el cual se va a mostrar en pantalla
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: 
                    paused = False
                elif event.key == pygame.K_g:  
                    save_actual_game(player, asteroids, shots, score)
                elif event.key == pygame.K_q:  
                    pygame.quit()
                    sys.exit()

        #Mostrar menu pausado
        font = pygame.font.Font(None, 36)
        pause_text = font.render("Pausa: Presione 'P' para reanudar, 'G' para guardar, 'Q' para salir", True, (255, 255, 255))
        screen.blit(pause_text, (SCREEN_WIDTH // 6, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        clock.tick(5)
