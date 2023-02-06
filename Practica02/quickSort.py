#QuickSort

def intercambia(A,x,y):
	tmp = A[x]
	A[x] = A[y]
	A[y] = tmp

def Particionar(A,p,r):
	pivote = lista[p]				#asignamos a una variable pivote la prinmera posición de la lista
	print(A)
	x = A[p]
	print(x)
	i = p
	for j in range(p+1, r+1):		#lo hace hasta r+1
		if (A[j] >= x):				#modificación para invertir el ordenamiento
			i = i+1
			intercambia(A,i,j)
	intercambia(A,i,p)
	return i

def QuickSort(A,p,r):
	if (p < r):
		q = Particionar(A,p,r)
		QuickSort(A,p,q-1)
		QuickSort(A,q+1,r)

lista = [2,9,1,7,10,4]
print("\nLista original: ")
print(lista)
QuickSort(lista,0,len(lista)-1)
print("\nLista ordenada: ")
print(lista)
