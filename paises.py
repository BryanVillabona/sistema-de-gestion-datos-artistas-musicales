from data import *

def registrar_pais(paises):
    codigo_pais = f"P-{len(paises) + 1:03d}"

    pais = input("Digite el nombre del país: ").strip().capitalize()
    if not pais:
        print("Error. El nombre no puede estar vacío.")
        return

    iso = input("Digite el código ISO (2 letras): ").strip().upper()
    iso3 = input("Digite el código ISO3 (3 letras): ").strip().upper()

    if not iso or not iso3 or len(iso) != 2 or len(iso3) != 3:
        print("Error. Código ISO inválido.")
        return

    paises[codigo_pais] = {
        "Codigo_Pais": codigo_pais,
        "Nombre_Pais": pais,
        "ISO": iso,
        "ISO3": iso3
    }

    guardar_datos(paises, "paises.json")
    print("***** País registrado correctamente. *****")




