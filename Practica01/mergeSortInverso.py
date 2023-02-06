#MergeSort inverso

def CrearSubArreglo(A, iIzq, iDer):
	return A[iIzq:iDer + 1]

def Merge(A,p,q,r):
	Izq = CrearSubArreglo(A,p,q)
	Der = CrearSubArreglo(A,q+1,r)
	i = 0
	j = 0
	for k in range(p,r+1):
		if (j >= len(Der)) or (i < len(Izq) and Izq[i] > Der[j]):
			A[k] = Izq[i]
			i = i + 1
		else:
			A[k] = Der[j]
			j = j + 1

def MergeSort(A,p,r):
	if r - p > 0:
		q = int((p+r)/2)
		MergeSort(A,p,q)
		MergeSort(A,q+1,r)
		Merge(A,p,q,r)

A = [6,12,4,9,5]
print("Lista inicial: ", A)
MergeSort(A, 0, len(A)-1)
print("Lista ordenada:", A)
