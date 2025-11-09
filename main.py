from funciones import *

ruta = "paises.csv"
paises = cargar_csv(ruta)

while True:
    print("----- MENÚ PRINCIPAL -----")
    print("1) Agregar un país")
    print("2) Actualizar un país")
    print("3) Buscar un país")
    print("4) Filtrar países por continente")
    print("5) Ordenar países por nombre")
    print("6) Mostrar estadísticas")
    print("0) Salir")

    opcion = input("Seleccione una opción: ").strip()

    match opcion:
        case "1": agregar_pais(paises, ruta)
        case "2": actualizar_pais(paises, ruta)
        case "3": buscar_por_nombre(paises, leer_texto_validado("Nombre o parte: "))
        case "4": filtrar_por_continente(paises)
        case "5": ordenar_por_nombre(paises)
        case "6": mostrar_estadisticas(paises)
        case "0":
            guardar_csv(ruta, paises)
            print("\nCambios guardados. Programa finalizado.\n")
            break
        case _:
            print("Opción inválida.\n")
