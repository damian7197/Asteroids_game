import json
import os
import re

archivo_usuarios = "./usuarios.json"

#verifica si el archivo existe, de ser asi lo hace en modo read y lo transforma a un diccionario en python
def cargar_usuarios():
    if os.path.exists(archivo_usuarios):
        with open(archivo_usuarios, 'r') as f:
            return json.load(f)
    return {}

#toma un diccionario de usuarios y lo convierte a json
def guardar_usuarios(usuarios):
    with open(archivo_usuarios, 'w') as f:
        json.dump(usuarios, f)
        
def password_valida(password):
    return re.match("^[a-zA-Z0-9]{8,}$", password) is not None 
    

#crea un usuario que va a ser almacenado dentro del archivo        
def crear_usuario(usuarios):
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario in usuarios:
        print("El nombre de usuario ya existe, intenta otro")
        return
    
    
    while True:
        password = input("Introduce tu contraseña(alfanumerica y al menos 8 caracteres): ")
        if not password_valida(password):
            print("La contraseña no es valida, intentelo otra vez")
            continue
        
        confirm_password = input("Confirme la contraseña ingresada")
        if password != confirm_password:
            print("Las contraseñas no coinciden, intentelo de nuevo")
        else: 
            #asignamos caracteristicas al usuario en su respectivo formato
            usuarios[nombre_usuario] = {'password': password, 'high_score': 0}
            guardar_usuarios(usuarios)
            print("El usuario ha sido creado con exito!")
            break


#valida el ingreso de usuarios existentes
def iniciar_sesion(usuarios):
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario in usuarios:
        password = input("Ingrese su contraseña: ")
        if usuarios[nombre_usuario]['password'] == password:
            print(f"Bienvenido a asteroides {nombre_usuario}")
            return usuarios[nombre_usuario] #retorno diccionario del usuario
        else:
            print("Contraseña incorrecta.")     
    else:
        print("Nombre de usuario incorrecto.")
    return None #no retorno nada si falla la autenticacion
        