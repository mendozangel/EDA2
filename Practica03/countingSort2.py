def countingSort(A):
    elemMax = int(max(A))
    elemMin = int(min(A))
    k = elemMax - elemMin + 1
    
    # Creamos un arreglo para almacenar los elementps e inicializar el arreglo en 0
    C = [0 for _ in range(k)]
    B = [0 for _ in range(len(A))]
 
    # Almacena el recuento de cada elemento que hay en el arreglo
    for i in range(0, len(A)):
        C[A[i]-elemMin] += 1
 
    # Cambia la posicion del arreglo para contener la posicion real del elemento en el arreglo de salida
    for i in range(1, len(C)):
        C[i] += C[i-1]
 
    # Contruye el arreglo para la salida
    for i in range(len(A)-1, -1, -1):
        B[C[A[i] - elemMin] - 1] = A[i]
        C[A[i] - elemMin] -= 1
 
    # Copia el arreglo de salida de modo que contiene los elementos ordenados
    for i in range(0, len(A)):
        A[i] = B[i]
 
    return A

A = [11, 15, 14, 29, 17, 20, 17]
print("Lista original: {}".format(A))
countingSort(A)
print("Lista ordenada: {}".format(A))