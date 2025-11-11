# 🌍 Gestión de Datos de Países en Python

## 🧩 Descripción del Programa

Este proyecto es una aplicación de consola desarrollada en **Python**, cuyo propósito es **gestionar información de países** a partir de un archivo CSV.  

Cada país se representa mediante los siguientes atributos:
- **Nombre**
- **Población**
- **Superficie**
- **Continente**

El programa permite realizar operaciones como **búsqueda**, **filtrado**, **ordenamiento**, **actualización de datos** y **cálculo de estadísticas**.  
Todos los datos ingresados son validados para evitar errores o inconsistencias (por ejemplo, campos vacíos o valores no numéricos).

---

## ⚙️ Requisitos

- Python **3.10 o superior** (se utiliza `match` en el menú).
- Archivo `paises.csv` ubicado en el mismo directorio que `main.py`.

---

## 🗂️ Estructura del Proyecto

```text
TPI-Programacion/
│
├── main.py                 # Control del flujo principal y menú interactivo
├── funciones.py            # Funciones de validación, búsqueda, ordenamiento y estadísticas
├── paises.csv              # Archivo CSV con los datos iniciales
│
└── docs/
    ├── Informe_TPI.pdf     # Informe teórico del trabajo
    ├── capturas/           # Capturas de pantalla del programa en ejecución
```
---

## 🧾 Formato del Archivo CSV

El archivo `paises.csv` debe tener la siguiente estructura:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

## 🚀 Ejecución del Programa

1. Abrir una terminal en la carpeta del proyecto.  
2. Ejecutar el siguiente comando:

   ```bash
   python main.py


### Menú Principal

```text
🌍  MENÚ PRINCIPAL  🌍
1- Agregar un país
2- Actualizar un país
3- Buscar un país
4- Filtrar países
5- Ordenar países
6- Mostrar estadísticas
0- Salir
```

## 💡 Ejemplos de Uso

### ➕ Agregar un país
**Entrada:**
```text
Nombre: Chile
Población: 19116209
Superficie: 756950
Continente: América
```

**Salida:**
```text
País agregado correctamente.
Chile | Población: 19116209 | Superficie: 756950 | Continente: América
```

### 🔍 Buscar un país
**Entrada:**
```text
Nombre o parte: jap
```
**Salida:**
```text
--- Resultado de la Búsqueda ---
Japón | Población: 125800000 | Superficie: 377975 | Continente: Asia
```

### 📊 Mostrar estadísticas
**Salida:**
```text
--- Estadísticas Generales ---
País con mayor población: Japón con 125800000
País con menor población: Argentina con 45376763
Promedio de población: 116067625.0
Promedio de superficie: 3084566.0 km²

Cantidad de países por continente:
- América: 2
- Europa: 1
- Asia: 1
```

## 👥 Participación de los Integrantes

| Integrante            | Comisión |
|-----------------------|-----------|
| Agustín S. Almonacid  | 12        |
| Brian Silvero         | 13        |

---