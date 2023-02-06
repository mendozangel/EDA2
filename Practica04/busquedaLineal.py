# Búsqueda Lineal o Secuencial

def busquedaLineal(A,n,x):
    encontrado = -1
    for k in range(n):
        if A[k] == x:
            encontrado=k
    return encontrado

# Búsqueda lineal Mejorada
def busquedaLinealMejorada(A,n,x):
    encontrado=-1
    for k in range(n):
        if A[k]==x:
            encontrado=k
            break
    return encontrado

#Búsqueda Lineal con Centinela
def busquedaLinealCentinela(A,n,x):
    tmp=A[n-1]
    A[n-1]=x
    k=0
    while A[k] != x:
        k=k+1
    print(k)
    A[n-1]=tmp
    if k < n or A[n]==x:
        return k
    else:
        return -1
    return encontrado

A=[9,5,-1,3,9,3,3]
print("La lista es: ")
print(A)

value = input("Introduce el valor a buscar: ")
x = int(value)
print("El numero por busqueda lineal:")
print(busquedaLineal(A,len(A),x))

value = input("Introduce el valor a buscar: ")
x = int(value)
print("El numero por busqueda lineal Mejorada:")
print (busquedaLinealMejorada(A,len(A),x))

value = input("Introduce el valor a buscar: ")
x = int(value)
print("El numero por busqueda lineal Centinela:")
print(busquedaLinealCentinela(A,len(A),x))
