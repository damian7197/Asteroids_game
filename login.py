import json
import os

def crear_usuario():
    pass

def iniciar_sesion():
    usuario = input("Ingrese su nombre de usuario: ").lower
    print(f"Bienvenido {usuario}!")
    password = input("Ingrese su contraseña: ")
    if password == password_correcta:
        print("Sesion iniciada")
    else:
        print("Contraseña incorrecta, intente otra vez")
        iniciar_sesion()
        
    

def main():
    
    while True:
        print("==========Bienvenido a asteroides!===========")
        print("1 - Crear un usuario nuevo")
        print("2 - Ingresar con usuario existente")
        print("3 - Salir del programa")
        opcion = input("Seleccione la opcion deseada (1,2,3):")
        
        if opcion == 1:
            crear_usuario()
        elif opcion == 2:
            iniciar_sesion()
        elif opcion == 3:
            print("Gracias por jugar asteroides! Hasta la proxima")
            break
        else:
            print("Opcion invalida, intentelo otra vez")
                






