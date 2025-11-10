from funciones import *

# === Códigos de color ANSI ===
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
GRAY = "\033[90m"

# === Funciones de interfaz ===

def mostrar_menu_principal():
    print(f"\n{BOLD}{BLUE}{'=' * 50}{RESET}")
    print(f"{BOLD}{CYAN}🌍  MENÚ PRINCIPAL  🌍{RESET}".center(50))
    print(f"{BLUE}{'=' * 50}{RESET}")
    print(f"{YELLOW}1){RESET} Agregar un país")
    print(f"{YELLOW}2){RESET} Actualizar un país")
    print(f"{YELLOW}3){RESET} Buscar un país")
    print(f"{YELLOW}4){RESET} Filtrar países por continente")
    print(f"{YELLOW}5){RESET} Ordenar países")
    print(f"{YELLOW}6){RESET} Mostrar estadísticas")
    print(f"{YELLOW}0){RESET} Salir")
    print(f"{BLUE}{'=' * 50}{RESET}")

def pausar():
    input(f"\n{GRAY}Presione ENTER para continuar...{RESET}")

def leer_opcion_valida(mensaje, opciones_validas):
    opcion = input(mensaje).strip()
    while opcion not in opciones_validas:
        print(f"{RED}❌ Error: opción inválida.{RESET}")
        opcion = input(mensaje).strip()
    return opcion

# === Programa principal ===

def main():
    ruta = "paises.csv"
    paises = cargar_csv(ruta)

    # --- Definición de funciones para cada opción ---
    def opcion_1():
        agregar_pais(paises, ruta)

    def opcion_2():
        actualizar_pais(paises, ruta)

    def opcion_3():
        buscar_por_nombre(paises, leer_texto_validado("Nombre o parte: "))

    def opcion_4():
        filtrar_por_continente(paises)

    def opcion_5():
        submenu_ordenar(paises)

    def opcion_6():
        mostrar_estadisticas(paises)

    # --- Diccionario de opciones ---
    opciones = {
        "1": opcion_1,
        "2": opcion_2,
        "3": opcion_3,
        "4": opcion_4,
        "5": opcion_5,
        "6": opcion_6,
    }

    # --- Bucle principal ---
    while True:
        mostrar_menu_principal()
        print(f"{MAGENTA}📊 Países cargados: {len(paises)}{RESET}")
        opcion = leer_opcion_valida(f"{BOLD}Seleccione una opción: {RESET}", list(opciones.keys()) + ["0"])

        if opcion == "0":
            guardar_csv(ruta, paises)
            print(f"\n{GREEN}💾 Cambios guardados. Programa finalizado.{RESET}\n")
            break
        else:
            opciones[opcion]()
            pausar()

# === Ejecución ===
if __name__ == "__main__":
    main()
