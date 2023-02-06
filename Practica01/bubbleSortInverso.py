#bubbleSort en orden inverso

def bubbleSortInv(A):
	pasadas = 0
	for i in range(1, len(A)):
		for j in range(len(A)-1):
			print(A)
			if A[j] < A[j+1]:	#En lugar de burbujear los mayores, burbujearemos los menores
				temp = A[j]
				A[j] = A[j+1]
				A[j+1] = temp
			pasadas = pasadas + 1
	print("Total de pasadas bubbleSort: {}\n".format(pasadas))


A = [10, 4, 1, 9]	# Declaro una lista A de 4 elementos
bubbleSortInv(A)		# Llamo al algoritmo bubbleSort y doy como parémetro la lista A
