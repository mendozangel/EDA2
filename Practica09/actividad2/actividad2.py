# Actividad propuesta por el profesor
import os

print("Ubicacion principal  ", os.getcwd())  # Para mostrar dónde estoy ubicado

# Definir una función para la creación de directorios / carpetas
def crearDirectorio(ruta):
    try:
        os.makedirs(ruta)
    except OSError:
        pass
    os.chdir(ruta)

# Creación de una carpeta de Probabilidad
crearDirectorio("./actividad2/Probabilidad")
file = open("./temario.txt", "w", encoding="utf-8")
file.write("***TEMARIO ***" + os.linesep)
file.write("1. Teoría de la probabilidad\n")
file.write("2. Variables aleatorias\n")
file.write("3. Variables aleatorias conjuntas.\n")
file.write("4. Modelos probabilisticos de fenómenos aleatorios discretos\n")
file.write("5. Modelos probabilisticos de fenómenos aleatorios continuos")
file.close()

print("Ubicacion actual  ", os.getcwd())   # Muestra la ubicación en la que estoy
print("Archivos guardados  ", os.listdir()) # Muestra los archivos guardados

os.chdir("/Users/ajmrz/OneDrive/Documents/EDA2/Practica10-AngelJesus-MendozaRodriguez") # Regreso a la carpeta
                                                                                        # donde guardaré mis directorios

# Creación de la carpeta de Ecuaciones Diferenciales
crearDirectorio("./actividad2/EcuacionesDiferenciales")
file = open("./temario.txt", "w", encoding="utf-8")
file.write("***TEMARIO ***" + os.linesep)
file.write("1. Ecuaciones diferenciales de primer orden lineales y no lineales\n")
file.write("2. Ecuaciones diferenciales lineales de orden superior\n")
file.write("3. Transformada de Laplace y sistemas de ecuaciones diferenciales lineales\n")
file.write("4. Introducción a las ecuaciones diferenciales en derivadas parciales")
file.close()

print("Ubicacion actual  ", os.getcwd())   # Muestra la ubicación en la que estoy
print("Archivos guardados  ", os.listdir()) # Muestra los archivos guardados

os.chdir("/Users/ajmrz/OneDrive/Documents/EDA2/Practica10-AngelJesus-MendozaRodriguez") # Regreso a mi carpeta principal

# Creación de la carpeta de Cálculo Vectorial
crearDirectorio("./actividad2/CalculoVectorial")
file = open("./temario.txt", "w", encoding="utf-8")
file.write("***TEMARIO ***" + os.linesep)
file.write("1. Máximos y mínimos de funciones de dos o más variables\n")
file.write("2. Funciones vectoriales\n")
file.write("3. Integrales de línea\n")
file.write("4. Integrales múltiples")
file.close()

print("Ubicacion actual  ", os.getcwd())   # Muestra la ubicación en la que estoy
print("Archivos guardados  ", os.listdir()) # Muestra los archivos guardados
os.chdir("/Users/ajmrz/OneDrive/Documents/EDA2/Practica10-AngelJesus-MendozaRodriguez") # Regreso a la carpeta principal

# Creación de la carpeta de EDA II
crearDirectorio("./actividad2/EDAII")
file = open("./temario.txt", "w", encoding="utf-8")
file.write("***TEMARIO ***" + os.linesep)
file.write("1. Algoritmos de ordenamiento\n")
file.write("2. Algoritmos de búsqueda\n")
file.write("3. Algoritmos de grafos\n")
file.write("4. Árboles\n")
file.write("5. Archivos\n")
file.write("6. Introducción a los algoritmos paralelos")
file.close()

print("Ubicacion actual  ", os.getcwd())   # Muestra la ubicación en la que estoy
print("Archivos guardados  ", os.listdir()) # Muestra los archivos guardados
os.chdir("/Users/ajmrz/OneDrive/Documents/EDA2/Practica10-AngelJesus-MendozaRodriguez") # Regreso a la carpeta principal

# Creación de la carpeta de POO
crearDirectorio("./actividad2/POO")
file = open("./temario.txt", "w", encoding="utf-8")
file.write("***TEMARIO ***" + os.linesep)
file.write("1. El paradigma orientado a objetos\n")
file.write("2. UML\n")
file.write("3. Tipos, expresiones y control de flujo\n")
file.write("4. Herencia y polimorfismo\n")
file.write("5. Manejo de excepciones y errores\n")
file.write("6. Flujo de entrada y salida\n")
file.write("7. Programación de hilos\n")
file.write("8. Introducción a patrones")
file.close()

print("Ubicacion actual  ", os.getcwd())   # Muestra la ubicación en la que estoy
print("Archivos guardados  ", os.listdir()) # Muestra los archivos guardados
os.chdir("/Users/ajmrz/OneDrive/Documents/EDA2/Practica10-AngelJesus-MendozaRodriguez") # Regreso a la carpeta principal
