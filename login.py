from usuarios import crear_usuario ,cargar_usuarios, iniciar_sesion
        

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
        opcion = input("Seleccione la opcion deseada (1,2,3):")
        print("==============================================")
        
        if opcion == "1":
            crear_usuario(usuarios)
        elif opcion == "2":
            iniciar_sesion(usuarios)
        elif opcion == "3":
            print("Gracias por jugar asteroides! Hasta la proxima")
            break
        else:
            print("Opcion invalida, intentelo otra vez")
            
if __name__=="__main__":
    main()
                






