from usuarios import crear_usuario ,cargar_usuarios, iniciar_sesion
        
    
#funcion principal login
def main():
    usuarios = cargar_usuarios()
    
    while True:
        print("==========Bienvenido a asteroides!===========")
        print("1 - Crear un usuario nuevo")
        print("2 - Ingresar con usuario existente")
        print("3 - Salir del programa")
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
                






