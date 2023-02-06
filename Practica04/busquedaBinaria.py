# Busqueda Binaria
import math

def BusquedaBin(A, x, izquierda, derecha):
    while izquierda <= derecha:
        medio = math.floor((izquierda + derecha)/2)
        if A[medio] == x:
            return medio
        elif A[medio] < x:
            izquierda = medio+1
        else:
            derecha = medio-1
    return -1

def bubbleSort(A):
    bandera = True
    pasada = 0
    while pasada < (len(A)-1) and bandera:
        bandera = False
        for j in range(len(A)-1-pasada):
            if (A[j] > A[j+1]):
                bandera = True
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp

A = [9,5,-1,3,9,3,3]
bubbleSort(A)   #Ordeno la lista       
value = int(input("Ingresa el valor que deseas buscar: "))
result = BusquedaBin(A,value,0,len(A)-1)    #Hago uso de Búsqueda Binaria

if result != -1:
    print("El elemento esta en el indice: " +    str(result) + ".")
    print(A)    #Imprimo la lista ordenada y verifico sí la respuesta anterior es correcta
else:
    print("No se encuentra el elemento.")

# Busqueda binaria Recursiva
def BusquedaBinRecursiva(A, x, izquierda, derecha):
    if izquierda > derecha:
        return -1
    medio = math.floor((izquierda+derecha)/2)

    if A[medio] == x:
        return medio
    elif A[medio] < x:
        return BusquedaBinRecursiva(A, x, medio+1, derecha)
    else:
        return BusquedaBinRecursiva(A, x, izquierda, medio-1)