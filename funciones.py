def cargar_csv(ruta):
    lista = []

    archivo = open(ruta, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    indice = 1  # Saltamos el encabezado
    while indice < len(lineas):
        linea = lineas[indice].strip()
        partes = linea.split(",")

        nombre = partes[0].strip()
        poblacion = int(partes[1].strip())
        superficie = int(partes[2].strip())
        continente = partes[3].strip()

        pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        lista.append(pais)
        indice += 1

    return lista


def guardar_csv(ruta, lista):
    archivo = open(ruta, "w", encoding="utf-8")
    archivo.write("nombre,poblacion,superficie,continente\n")

    indice = 0
    while indice < len(lista):
        pais = lista[indice]
        linea = pais["nombre"] + "," + str(pais["poblacion"]) + "," + str(pais["superficie"]) + "," + pais["continente"] + "\n"
        archivo.write(linea)
        indice += 1

    archivo.close()


# VALIDACIONES -------------------------------------------------------

def normalizar_titulo_simple(texto):
    texto = texto.strip()
    partes = texto.split()
    resultado = []

    indice = 0
    while indice < len(partes):
        palabra = partes[indice]
        primera = palabra[0].upper()
        resto = palabra[1:].lower()
        palabra_final = primera + resto
        resultado.append(palabra_final)
        indice += 1

    return " ".join(resultado)


def es_letras_y_espacios(cadena):
    indice = 0
    hay_letra = False

    while indice < len(cadena):
        caracter = cadena[indice]

        if caracter.isalpha():
            hay_letra = True
        elif caracter != " ":
            return False

        indice += 1

    return hay_letra


def confirmar_valor(valor):
    respuesta = input(f"Ingresó '{valor}'. ¿Desea usar ese valor igualmente? (S/N): ").strip().upper()

    while respuesta != "S" and respuesta != "N":
        print("Error: solo se permite responder S o N.")
        respuesta = input(f"¿Confirma usar '{valor}'? (S/N): ").strip().upper()

    return respuesta == "S"


def leer_texto_validado(mensaje):
    texto = input(mensaje).strip()

    while texto == "" or not es_letras_y_espacios(texto):
        print("Error: ingrese solo letras y espacios.")
        texto = input(mensaje).strip()

    # Contar letras para validar textos muy cortos
    cantidad = 0
    indice = 0
    while indice < len(texto):
        if texto[indice].isalpha():
            cantidad += 1
        indice += 1

    if cantidad < 3:
        if confirmar_valor(texto) == False:
            return leer_texto_validado(mensaje)

    return normalizar_titulo_simple(texto)


def leer_entero_positivo(mensaje):
    dato = input(mensaje).strip()
    while not dato.isdigit():
        print("Error: ingrese un número entero no negativo.")
        dato = input(mensaje).strip()
    return int(dato)


def seleccionar_continente():
    print("\nSeleccione un continente:")
    print("1) América")
    print("2) Europa")
    print("3) Asia")
    print("4) África")
    print("5) Oceanía")
    print("6) Antártida\n")

    opcion = input("Opción: ").strip()

    while opcion not in ["1", "2", "3", "4", "5", "6"]:
        print("Error: seleccione una opción válida del 1 al 6.")
        opcion = input("Opción: ").strip()

    match opcion:
        case "1": return "América"
        case "2": return "Europa"
        case "3": return "Asia"
        case "4": return "África"
        case "5": return "Oceanía"
        case "6": return "Antártida"


# MOSTRAR LISTA -----------------------------------------------------

def mostrar_lista_completa(lista):
    print("\n--- Lista de Países ---")

    if len(lista) == 0:
        print("No hay países cargados.\n")
        return

    indice = 0
    while indice < len(lista):
        pais = lista[indice]
        print(pais["nombre"], "| Población:", pais["poblacion"], "| Superficie:", pais["superficie"], "| Continente:", pais["continente"])
        indice += 1

    print()


# OPERACIONES -------------------------------------------------------

def existe_pais(lista, nombre):
    indice = 0
    while indice < len(lista):
        if lista[indice]["nombre"].lower() == nombre.lower():
            return True
        indice += 1
    return False


def agregar_pais(lista, ruta_csv):
    print("\n--- Agregar País ---")

    nombre = leer_texto_validado("Nombre: ")

    if existe_pais(lista, nombre):
        print("Ya existe un país con ese nombre.\n")
        return

    continente = seleccionar_continente()
    poblacion = leer_entero_positivo("Población: ")
    superficie = leer_entero_positivo("Superficie: ")

    pais = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
    lista.append(pais)

    guardar_csv(ruta_csv, lista)

    print("\nPaís agregado correctamente.")
    mostrar_lista_completa(lista)


def buscar_por_nombre(lista, texto):
    print("\n--- Resultado de la Búsqueda ---")
    texto = texto.lower()
    encontrado = False

    indice = 0
    while indice < len(lista):
        pais = lista[indice]
        if texto in pais["nombre"].lower():
            encontrado = True
            print(pais["nombre"], "| Población:", pais["poblacion"], "| Superficie:", pais["superficie"], "| Continente:", pais["continente"])
        indice += 1

    if not encontrado:
        print("No se encontraron coincidencias.\n")
    print()


def actualizar_pais(lista, ruta_csv):
    print("\n--- Actualizar País ---")

    print("Lista de países disponibles:")
    mostrar_lista_completa(lista)

    nombre = leer_texto_validado("Nombre del país a actualizar: ")

    indice = 0
    encontrado = False

    while indice < len(lista):
        pais = lista[indice]
        if pais["nombre"].lower() == nombre.lower():
            encontrado = True
            pais["poblacion"] = leer_entero_positivo("Nueva población: ")
            pais["superficie"] = leer_entero_positivo("Nueva superficie: ")
            guardar_csv(ruta_csv, lista)
            print("\nPaís actualizado correctamente.\n")
        indice += 1

    if not encontrado:
        print("No existe un país con ese nombre.\n")


def filtrar_por_continente(lista):
    continente = seleccionar_continente().lower()
    print("\n--- Filtro por Continente ---")

    encontrado = False
    indice = 0
    while indice < len(lista):
        pais = lista[indice]
        if pais["continente"].lower() == continente:
            encontrado = True
            print(pais["nombre"], "|", pais["continente"])
        indice += 1

    if not encontrado:
        print("No se encontraron países para ese continente.\n")
    print()


# ORDENAMIENTOS ------------------------------------------------------

def ordenar_por_nombre(lista):
    i = 0
    while i < len(lista) - 1:
        j = i + 1
        while j < len(lista):
            if lista[i]["nombre"].lower() > lista[j]["nombre"].lower():
                t = lista[i]
                lista[i] = lista[j]
                lista[j] = t
            j += 1
        i += 1


def ordenar_por_poblacion_menor_a_mayor(lista):
    i = 0
    while i < len(lista) - 1:
        j = i + 1
        while j < len(lista):
            if lista[i]["poblacion"] > lista[j]["poblacion"]:
                t = lista[i]
                lista[i] = lista[j]
                lista[j] = t
            j += 1
        i += 1


def ordenar_por_poblacion_mayor_a_menor(lista):
    i = 0
    while i < len(lista) - 1:
        j = i + 1
        while j < len(lista):
            if lista[i]["poblacion"] < lista[j]["poblacion"]:
                t = lista[i]
                lista[i] = lista[j]
                lista[j] = t
            j += 1
        i += 1


def ordenar_por_superficie_menor_a_mayor(lista):
    i = 0
    while i < len(lista) - 1:
        j = i + 1
        while j < len(lista):
            if lista[i]["superficie"] > lista[j]["superficie"]:
                t = lista[i]
                lista[i] = lista[j]
                lista[j] = t
            j += 1
        i += 1


def ordenar_por_superficie_mayor_a_menor(lista):
    i = 0
    while i < len(lista) - 1:
        j = i + 1
        while j < len(lista):
            if lista[i]["superficie"] < lista[j]["superficie"]:
                t = lista[i]
                lista[i] = lista[j]
                lista[j] = t
            j += 1
        i += 1


def submenu_ordenar(lista):
    print("\n--- Ordenar Países ---")
    print("1) Por nombre (A-Z)")
    print("2) Por población (menor → mayor)")
    print("3) Por población (mayor → menor)")
    print("4) Por superficie (menor → mayor)")
    print("5) Por superficie (mayor → menor)")
    print("0) Volver\n")

    opcion = input("Seleccione una opción: ").strip()

    match opcion:
        case "1":
            ordenar_por_nombre(lista)
            print("\nOrdenados por nombre (A-Z):")
            mostrar_lista_completa(lista)

        case "2":
            ordenar_por_poblacion_menor_a_mayor(lista)
            print("\nOrdenados por población (menor → mayor):")
            mostrar_lista_completa(lista)

        case "3":
            ordenar_por_poblacion_mayor_a_menor(lista)
            print("\nOrdenados por población (mayor → menor):")
            mostrar_lista_completa(lista)

        case "4":
            ordenar_por_superficie_menor_a_mayor(lista)
            print("\nOrdenados por superficie (menor → mayor):")
            mostrar_lista_completa(lista)

        case "5":
            ordenar_por_superficie_mayor_a_menor(lista)
            print("\nOrdenados por superficie (mayor → menor):")
            mostrar_lista_completa(lista)

        case "0":
            print()
        case _:
            print("Opción inválida.\n")


# ESTADÍSTICAS ------------------------------------------------------

def mostrar_estadisticas(lista):
    print("\n--- Estadísticas Generales ---")

    if len(lista) == 0:
        print("No hay datos disponibles.\n")
        return

    # Mayor y menor población
    mayor = lista[0]
    menor = lista[0]

    indice = 0
    while indice < len(lista):
        pais = lista[indice]
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais
        indice += 1

    # Promedio de superficie
    total_superficie = 0
    total_poblacion = 0
    indice = 0
    while indice < len(lista):
        total_superficie += lista[indice]["superficie"]
        total_poblacion += lista[indice]["poblacion"]
        indice += 1

    promedio_superficie = total_superficie / len(lista)
    promedio_poblacion = total_poblacion / len(lista)

    # Cantidad por continente
    conteo = {}
    indice = 0
    while indice < len(lista):
        cont = lista[indice]["continente"]
        if cont not in conteo:
            conteo[cont] = 1
        else:
            conteo[cont] = conteo[cont] + 1
        indice += 1

    print("País con mayor población:", mayor["nombre"], "con", mayor["poblacion"])
    print("País con menor población:", menor["nombre"], "con", menor["poblacion"])
    print("Promedio de población:", round(promedio_poblacion, 2))
    print("Promedio de superficie:", round(promedio_superficie, 2), "km²\n")

    print("Cantidad de países por continente:")
    for continente in conteo:
        print("-", continente + ":", conteo[continente])

    print()
