# procedimiento o funcion para obtener k
def obtenerK(A):
	elemMax = int(max(A))
	elemMin = int(min(A))
	k = elemMax - elemMin
	return int(k)

def countingSort(A,k):
	C = [0 for _ in range(k+1)]
	B = [0 for _ in range(len(A))]

	for j in range(0,len(A)):
		C[A[j]] += 1

	for i in range(1,k+1):
		C[i] += C[i-1]

	for j in range(len(A)-1,-1,-1):
		B[C[A[j]]-1] = A[j]
		C[A[j]] -= 1
	return B

A = [11,15,14,29,17,20,17]

valorK = obtenerK(A)
print("Lista original: {}".format(A))
countingSort(A,valorK)
