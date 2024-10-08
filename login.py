import json
import os

archivo_usuarios = "usuarios.json"

def cargar_usuarios():
    if os.path.exists(archivo_usuarios):
        with open(archivo_usuarios, 'r') as f:
            return json.load(f)
    return {}

def guardar_usuarios(usuarios):
    with open(archivo_usuarios, 'w') as f:
        json.dump(usuarios, f)
        
def crear_usuario(usuarios):
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario in usuarios:
        print("El nombre de usuario ya existe, intenta otro")
    else:
        password = input("Introduce tu contraseña: ")
        usuarios[nombre_usuario] = {'password': password, 'high_score': 0}

def iniciar_sesion(usuarios):
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario in usuarios:
        password = input("Ingrese su contraseña: ")
        if usuarios[nombre_usuario]['password'] == password:
            print(f"Bienvenido a asteroides {nombre_usuario}")
        else:
            print("Contraseña incorrecta.")     
    else:
        print("Nombre de usuario incorrecto.")
        
    

def main():
    usuarios = cargar_usuarios()
    
    while True:
        print("==========Bienvenido a asteroides!===========")
        print("1 - Crear un usuario nuevo")
        print("2 - Ingresar con usuario existente")
        print("3 - Salir del programa")
        opcion = input("Seleccione la opcion deseada (1,2,3):")
        
        if opcion == 1:
            crear_usuario(usuarios)
        elif opcion == 2:
            iniciar_sesion(usuarios)
        elif opcion == 3:
            print("Gracias por jugar asteroides! Hasta la proxima")
            break
        else:
            print("Opcion invalida, intentelo otra vez")
                






