from data import *

def registrar_pais():
    codigo_pais = f"P-{len(paises)+1:03d}"

    pais = input("Digite el nombre del pais: ").strip().capitalize()
    if not pais:
        raise ValueError("Error. El nombre no puede estar vacio")
    
    paises[codigo_pais] = {
        "Codigo_Pais": codigo_pais,
        "Nombre_Pais": pais
    }
    guardar_datos(paises, "paises.json")
    print("************Pais registrado************")



