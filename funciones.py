def cargar_csv(ruta):
    lista = []

    archivo = open(ruta, "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    indice = 1  # Saltamos encabezado
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
        resultado.append(primera + resto)
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

    # Contar letras
    letras = 0
    indice = 0
    while indice < len(texto):
        if texto[indice].isalpha():
            letras += 1
        indice += 1

    if letras < 3:
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
    print("6) Antártida")

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


# OPERACIONES -------------------------------------------------------

def existe_pais(lista, nombre):
    indice = 0
    while indice < len(lista):
        if lista[indice]["nombre"].strip().lower() == nombre.strip().lower():
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
    print("Datos registrados:")
    print("Nombre:", nombre)
    print("Continente:", continente)
    print("Población:", poblacion)
    print("Superficie:", superficie, "\n")


def buscar_por_nombre(lista, texto):
    print("\n--- Resultado de la Búsqueda ---")
    texto = texto.strip().lower()
    encontrado = False

    indice = 0
    while indice < len(lista):
        pais = lista[indice]
        if texto in pais["nombre"].strip().lower():
            encontrado = True
            print(pais["nombre"], "|", pais["poblacion"], "|", pais["superficie"], "|", pais["continente"])
        indice += 1

    if not encontrado:
        print("No se encontraron coincidencias.\n")


def actualizar_pais(lista, ruta_csv):
    print("\n--- Actualizar País ---")

    if len(lista) == 0:
        print("No hay países cargados.\n")
        return

    print("Lista de países disponibles:")
    indice = 0
    while indice < len(lista):
        print("-", lista[indice]["nombre"])
        indice += 1

    nombre = leer_texto_validado("\nNombre del país a actualizar: ")

    indice = 0
    encontrado = False

    while indice < len(lista):
        pais = lista[indice]
        if pais["nombre"].strip().lower() == nombre.strip().lower():
            encontrado = True

            pais["poblacion"] = leer_entero_positivo("Nueva población: ")
            pais["superficie"] = leer_entero_positivo("Nueva superficie: ")

            guardar_csv(ruta_csv, lista)

            print("\nPaís actualizado correctamente.")
            print("Nombre:", pais["nombre"])
            print("Nueva población:", pais["poblacion"])
            print("Nueva superficie:", pais["superficie"], "\n")
            return
        indice += 1

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


def ordenar_por_nombre(lista):
    print("\n--- Ordenar por Nombre (A-Z) ---")

    i = 0
    while i < len(lista) - 1:
        j = i + 1
        while j < len(lista):
            if lista[i]["nombre"].lower() > lista[j]["nombre"].lower():
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
            j += 1
        i += 1

    print("Lista ordenada correctamente.\n")


def mostrar_estadisticas(lista):
    print("\n--- Estadísticas Generales ---")

    if len(lista) == 0:
        print("No hay datos disponibles.\n")
        return

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

    total_superficie = 0
    indice = 0
    while indice < len(lista):
        total_superficie += lista[indice]["superficie"]
        indice += 1

    promedio = total_superficie / len(lista)

    print("País con mayor población:", mayor["nombre"])
    print("País con menor población:", menor["nombre"])
    print("Promedio de superficie:", round(promedio, 2), "\n")
