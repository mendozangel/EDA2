# Busqueda lineal recursiva

def busquedaLinealRecursiva(A, x, inicio, fin):
    if inicio > fin:
        encontrado = -1
    else:
        if A[inicio] == x:
            encontrado = inicio
        else:
            encontrado = busquedaLinealRecursiva(A, x, inicio+1, fin)
    return encontrado

A = [9, 5, -1, 3, 9, 3, 3]

value = int(input("Ingrese el valor que deseas buscar: "))
encontrado = busquedaLinealRecursiva(A, value, 0, len(A)-1)

if (encontrado == -1):
    print("*El elemento no encontrado*")
else:
    print("El elemento se encuentra en el indice: ", encontrado)
