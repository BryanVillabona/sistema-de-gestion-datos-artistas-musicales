import json

paises = {}
generos = {}
artistas = {}

import json

def cargar_datos(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"No se pudo cargar datos de {archivo}. Error: {e}")
        return None

def guardar_datos(datos, archivo):
    try:
        with open(archivo, "w", encoding="utf-8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"No se pudo guardar datos en {archivo}. Error: {e}")
