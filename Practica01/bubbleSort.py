#Actividad 1. BubbleSort

def bubbleSort(A):
	pasadas = 0
	for i in range(1, len(A)):
		for j in range(len(A)-1):
			print(A)
			if A[j] > A[j+1]:
				temp = A[j]
				A[j] = A[j+1]
				A[j+1] = temp
			pasadas = pasadas+1
	print("Total de pasadas bubbleSort: {}\n".format(pasadas))

def bubbleSort2(A):
	bandera = True
	pasada = 0
	totalPasadas = 0 
	while pasada < len(A)-1 and bandera:
		bandera = False
		for j in range(len(A)-1-pasada):
			print(A)
			if(A[j] > A[j+1]):
				bandera = True
				temp = A[j]
				A[j] = A[j+1]
				A[j+1] = temp
			totalPasadas = totalPasadas + 1
	print("Total de pasadas: {}".format(totalPasadas))

A = [10, 4, 1, 9]	# Declaro una lista A de 4 elementos
#bubbleSort(A)		# Llamar al algoritmo bubbleSort y doy como parémetro la lista A
bubbleSort2(A)		# Ahora llamo al algoritmo bubbleSort2 y de igual manera doy como parámetro a la lista A