from data import *

def registrar_genero():
    codigo_genero = f"G-{len(generos)+1:03d}"

    genero = input("Digite el nombre del genero: ").strip().capitalize()
    if not genero:
        raise ValueError("Error. El nombre no puede estar vacio")
    
    generos[codigo_genero] = {
        "Codigo_Genero": codigo_genero,
        "Nombre_Genero": genero
    }
    guardar_datos(generos, "generos.json")
    print("************Genero registrado************")