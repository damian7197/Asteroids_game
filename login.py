from usuarios import crear_usuario ,cargar_usuarios, iniciar_sesion
from game_logic import game
from high_scores import mostrar_high_scores       

# Funcion para cargar el menú desde un archivo
def cargar_menu(filename):
    with open(filename, 'r') as file:
        opciones = file.readlines()
    return [opcion.strip() for opcion in opciones]    

#funcion principal login
def main():
    usuarios = cargar_usuarios()
    menu_opciones = cargar_menu('menu.txt')
    
    while True:
        print("==========Bienvenido a asteroides!===========")
        for opcion in menu_opciones:
            print(opcion)
        opcion = input("Seleccione la opcion deseada (1,2,3,4): ")
        print("==============================================")
        
        if opcion == "1":
            crear_usuario(usuarios)
        elif opcion == "2":
            usuario_actual = iniciar_sesion(usuarios)
            if usuario_actual:
                print(f"Inicio de sesion exitoso, comenzando el juego como {usuario_actual}")
                game(usuario_actual)
        elif opcion == "3":
            print("Gracias por jugar asteroides! Hasta la proxima")
            break
        elif opcion == "4":
            mostrar_high_scores()
        else:
            print("Opcion invalida, intentelo otra vez")
            
if __name__=="__main__":
    main()
                






