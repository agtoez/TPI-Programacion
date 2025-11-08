# Gestión de Datos de Países en Python

## Descripción del Programa

Este proyecto consiste en una aplicación de consola desarrollada en Python, cuyo objetivo es gestionar información de países a partir de un archivo CSV.  
Cada país se representa mediante cuatro atributos fundamentales: **nombre**, **población**, **superficie** y **continente**.

El programa lee los datos iniciales desde el archivo `paises.csv` y los almacena en una **lista de diccionarios**, lo que permite realizar operaciones de búsqueda, filtrado, ordenamiento y cálculo de estadísticas de manera clara y estructurada.  
Se implementan **validaciones en todas las entradas**, evitando campos vacíos o valores numéricos inválidos para garantizar la integridad de los datos.

---

## Requisitos

- Python **3.10 o superior** (se utiliza `match` en el menú).
- Archivo `paises.csv` ubicado en el mismo directorio que `main.py`.

---

## Estructura del Proyecto

TPI-Programacion
│
├─ main.py # Menú principal y control del flujo del programa
├─ funciones.py # Validaciones, búsqueda, filtrado, ordenamiento y estadísticas
├─ paises.csv # Dataset inicial cargado por el sistema
│
└─ docs
├─ Informe_TPI.pdf # Informe teórico del trabajo integrador
├─ capturas/ # Capturas de pantalla del programa funcionando
└─ diagrama/ # Diagrama del funcionamiento del sistema


## Formato del Archivo CSV

El archivo `paises.csv` debe contener las siguientes columnas:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa

## Ejecución del Programa
1- Abrir una terminal en la carpeta del proyecto.

2- Ejecutar:
	python main.py

Menú Principal
1- Agregar un país: Solicita todos los datos con validación (texto no vacío, enteros ≥ 0).
2- Actualizar un país: Permite modificar población y superficie de un país existente.
3- Buscar un país: Búsqueda por coincidencia parcial, sin distinguir mayúsculas/minúsculas.
4- Filtrar países: Por continente, rango de población o rango de superficie.
5- Ordenar países: Por nombre, población o superficie (ascendente o descendente).
6- Mostrar estadísticas: Máx/mín población, promedios y cantidad de países por continente.
0- Salir: Finaliza el programa.

Ejemplos reales del programa: 

El formato para agregar un país es el siguiente: 
Nombre: Chile
Continente: América
Población: 19116209
Superficie: 756102
País agregado correctamente.

El formato para buscar un pais es el siguiente:
Nombre: Argentina
Resultado: 
Nombre: Argentina | Población: 45376763 | Superficie: 2780400 | Continente: América


El formato de resultado de la opcion de Estadisticas es: 
País con mayor población: Brasil
País con menor población: Alemania
Promedio de población: 111079875.75

## Participación de los Integrantes
- Agustin S. Almonacid - Comision 12
- Brian Silvero - Comision 13












# Trabajo Práctico Integrador de Programación.

Alumnos: 
	- Brian David Silvero – Comisión 13
	- Agustín Tomás Ezequiel Sánchez Almonacid – Comisión 12
