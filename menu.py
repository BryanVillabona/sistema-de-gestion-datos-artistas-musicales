from paises import registrar_pais
from generos import registrar_genero
from artistas import registrar_artista

menu_principal = """
******************************************
1. Gestion de datos de artistas musicales
2. Registro de paises
3. Registro de generos
4. Salir
******************************************
"""

menu_datos_artistas = """
*****************************
1. Registrar artista
2. Generar informes
3. Regresar
*****************************
"""

def mostrar_menu_principal():
    return print(menu_principal)

def mostrar_menu_datos_artistas():
    return print(menu_datos_artistas)

def menu_principal_mostrar():
    
    while True:
        mostrar_menu_principal()
        opc_principal = int(input("Bienvenido. Elija una opcion: "))
        match opc_principal:
            case 1:
                artistas_menu()
            case 2:
                registrar_pais()
            case 3:
                registrar_genero()
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Error. Elija una opcion valida")

def artistas_menu():
    
    while True:
            mostrar_menu_datos_artistas()
            opcion_artista = int(input("Elija una opcion: "))
            match opcion_artista:
                case 1:
                    registrar_artista()
                case 2:
                    print("consultas")
                case 3:
                    print("Regresar")
                    break
                case _:
                    print("Error. Elija una opcion valida")