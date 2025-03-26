import json

paises = {}
generos = {}
artistas = {}

def cargar_datos(archivo):
    datos = {}
    try:
        with open(archivo, "r") as file:
            datos = json.load(file)
    except Exception:
        print("No se pudo cargar datos")

        datos = None
    
    if archivo == "paises.json":
        paises.update(datos)
    elif archivo == "artistas.json":
        artistas.update(datos)
    elif archivo == "generos.json":
        generos.update(datos)

def guardar_datos(datos, archivo):
    try:
        datos_a_guardar = json.dumps(datos, indent=4)
        with open(archivo, "w") as file:
            file.write(datos_a_guardar)

    except Exception:
        print("No se pudo guardar datos")