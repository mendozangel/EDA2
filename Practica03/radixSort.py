#radix Sort
def formaListaConClaves(B,numCar):
	Btmp = []
	D = {}
	j = 0
	for i in range(48,58):
		D[chr(i)]=j
		j+=1

	for i in range(65,91):
		D[chr(i)]=j
		j+=1

	for i in range(len(B)):
		Btmp.append([B[i]]*2)
		A3=list(B[i])
		Btmp[i][1]=D[A3[numCar-1]]
	return Btmp

def countingSort2(A,k):
	C=[0 for _ in range(k+1)]
	B=[list (0 for _ in range(2)) for _ in range(len(A))]
	for j in range(0,len(A)):
		C[A[j][1]] = C[A[j][1]]+1

	for i in range(1,k+1):
		C[i]=C[i]+C[i-1]

	for j in range(len(A)-1,-1,-1):
		B[C[A[j][1]]-1][1]=A[j][1]
		B[C[A[j][1]]-1][0]=A[j][0]
		C[A[j][1]]=C[A[j][1]]-1
	return B

def obtenerElemSinClaves(E):
	Elem=[]
	for i in range(0,len(E)):
		Elem.append(E[i][0])
	return Elem

def radixSort(A):
	numCar=len(A[1])
	#for i in range(numCar,0,-1):			radixSort de forma original
	for i in range(1,numCar+1,1):			#modificación para un radixSort inverso
		cc = formaListaConClaves(A,i)
		ordenado = countingSort2(cc,36)
		A = obtenerElemSinClaves(ordenado)
	return A

def main():
	lista=['XI7FS6','PL4ZQ2','JI8FR9','XL8FQ6','PY2ZR5','KV7WS9','JL2ZV3','KI4WR2']
	A = radixSort(lista)
	print('\n\nLista ordenada: \n', A)
main()
