from data import *

def registrar_artista():
    codigo_artista = f"A-{len(artistas)+1:03d}"

    artista = input("Digite el nombre del artista: ").strip().capitalize()
    if not artista:
        raise ValueError("Error. El nombre no puede estar vacio")
    
    pais = input("Digite el pais del artista: ").strip().capitalize()
    if not pais:
        raise ValueError("Error. El pais no puede estar vacio")

    anios_actividad = input("Digite los anios de actividad del artista: ").strip()
    if not anios_actividad:
        raise ValueError("Error. El nombre no puede estar vacio")
    
    anio_lanzamiento_primer_disco = input("Digite el anio de lanzamiento del primer disco del artista: ").strip()
    if not anio_lanzamiento_primer_disco:
        raise ValueError("Error. El nombre no puede estar vacio")
    
    genero_musical = input("Digite el genero musical del artista: ").strip().capitalize()
    if not genero_musical:
        raise ValueError("Error. El nombre no puede estar vacio")
    
    unidades_certificadas_totales = input("Digite las unidades certificadas totales: ").strip()
    if not unidades_certificadas_totales:
        raise ValueError("Error. El nombre no puede estar vacio")
    
    ventas_reclamadas = input("Digite las ventas reclamadas del artista: ").strip()
    if not ventas_reclamadas:
        raise ValueError("Error. El nombre no puede estar vacio")
    
    while True:
        try:
            elegir = int(input("Elija 1. Para activo o 2. para inactivo: "))
            if elegir == 1:
                activo = "Activo"
                break
            elif elegir == 2:
                activo = "Inactivo"
                break
            else:
                print("Elija una opcion valida")
        except Exception:
            print("Error. Debe digitar 1 o 2 segun sea el caso")

    artistas[codigo_artista] = {
        "Nombre_Artista": artista,
        "Nombre_Pais": pais,
        "Anios_Actividad": anios_actividad,
        "Lanzamiento_Primer_Disco": anio_lanzamiento_primer_disco,
        "Genero_Musical": genero_musical,
        "Unidades_Certificadas_Totales": unidades_certificadas_totales,
        "Ventas_Reclamadas": ventas_reclamadas,
        "Estado": activo

    }
    guardar_datos(artistas, "artistas.json")
    print("************Genero registrado************")