/* Version paralela*/
#include <stdio.h>
#include <omp.h>

int buscaMaximo(int *a, int n) {
	int max,i;
	max = a[0];
	# pragma omp parallel for
	for(i=0; i<n; i++){
		if(a[i] > max){
			#pragma omp critical
			{
				if(a[i] > max)
				max = a [i];
			}
		}
	}
}

int main(){
	int a[5] = {14,22,5,12,3};
	int m = buscaMaximo(a, 5);
	printf("El maximo del arreglo es: %d\n", m);
	return 0;
}
