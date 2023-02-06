# Ejercicio Propuesto por el profesor

def busquedaLinealR(A,n,x):
    encontrado = 1
    c = 0
    for k in range (n):
        if A[k] == x:
            encontrado = k
            c += 1
            print("El número se encuentra en la posición:", k, "de la lista.")
    return encontrado

A = [9,5,-1,3,9,3,3]
print(A)
value = int(input("Ingresa el valor que deseas buscar: "))
print(busquedaLinealR(A, len(A), value))
