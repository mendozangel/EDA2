import locale
import pickle
import os

# Revisar el formato de codificación del sistema
print("Codificación  ", locale.getpreferredencoding())

# Estructura general con manejo de excepciones. Método open() y cerrar archivo.
try:
	archivo = open("./p10/prueba.txt", "r", encoding="utf-8")
	# Realizar operaciones con el archivo
except:
	print("error al abrir.")
finally:
	if archivo:
		archivo.close

# Método read()
archivo = open("./p10/prueba.txt", "r")
c1 = archivo.read(2)
c2 = archivo.read()
print("Impresion Método read()  ", c1)
#print(c2)
archivo.close()

# Método readline()
a3 = open("./p10/prueba.txt", "r")
while True:
	linea = a3.readline()
	if not linea:
		break
	print("Impresion Método readLine()  ", linea)
a3.close()

# Método readlines()
archivo = open("./p10/prueba.txt", "r")
lista = archivo.readlines()  # lee todas las lineas a una lista
numlin = 0
for linea in lista:
	numlin += 1
	print("Impresion Método readlines()  ", numlin, linea)
archivo.close()

# Sentencia with-as
with open("./p10/prueba.txt", "r") as archivo:
	for linea in archivo:	# recorre linea a linea el archivo
		print("Impresion sentencia with-as  ", linea)

# Método write
cadena1 = 'Datos'	# declara cadena1
cadena2 = 'Secretos'	# declara cadena2
archivo2 = open("./p10/datos2.txt", "w")	# abre archivo para escribir
print('Impresión cadena 1  ' + cadena1 + '\n')	# impresion de la cadena1
archivo2.write(cadena1 + '\n')	# escribe cadena1 añadiendo salto de linea
archivo2.write("hola")	# escribe la cadena hola
archivo2.write(cadena2)	# escribe cadena2 en archivo
archivo2.close			# cierra archivo

# Método writelines()
lista = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']	# declara lists
archivo2 = open("./p10/datos2.txt", "w")	# abre archivo en modo escritura
archivo2.writelines(lista)	# escribe la lista en el archivo
archivo2.close()

# Método seek
archivo = open("./p10/prueba.txt", "r")
archivo.seek(5)	# mueve el puntero al quinto byte
cadena1 = archivo.read(5)	# lee los siguientes 5 bytes
print(cadena1)	# muestra la cadena
print("Posicion del puntero  ", archivo.tell(), "\n")	# muestra la posición del puntero
archivo.close()	# cierra el archivo

# Modulo pickle
lista = ["algoritmos 1", "algoritmos 2", "estructuras"]	# declara lista
archivo = open("./p10/materias.dat", "wb")	# abre archivo binario para escribir
pickle.dump(lista, archivo)	# escribe lista en el archivo
archivo.close()	# cierra el archivo
del lista	# borra de memoria la lista
archivo = open("./p10/materias.dat", "rb")	# abre el archivo binario para leer
lista = pickle.load(archivo)	# carga lista desde archivo
print(lista, "\n")	# muestra la lista
archivo.close	# cierra el archivo

# Conocer los atributos de un archivo

archivo = open("./p10/prueba.txt", "r")
contenido = archivo.read()
nombre = archivo.name
modo = archivo.mode
codificacion = archivo.encoding
archivo.close()

if archivo.closed:
    print("El archivo se ha cerrado correctamente.\n")
else:
    print("El archivo permanece abierto.\n")

print("*** Atributos del archivo ***")
print("Contenido: ", contenido)
print("Nombre:  ", nombre)
print("Modo:  ", modo)
print("Codificación:  ", codificacion)

# Crear diretorio
def crear_directorio(ruta):
    try:
        os.makedirs(ruta)
    except OSError:
        pass
    os.chdir(ruta)

crear_directorio("./p10/nuevo")

# Recorrer un directorio
rootDir = "./p10"
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Directorio encontrado: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
