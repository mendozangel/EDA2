/* Versión serial */
#include <stdio.h>
#include <omp.h>

double empezar, terminar;

int main(){
	int a[500][500], b[500][500], c[500][500];

	for(int i=0; i<500; i++) {
		for(int j=0; j<500; j++) {
			a[i][j] = j+2;
			b[i][j] = j-3;
		}
	}
    empezar=omp_get_wtime();
	int i,j,k;
	for(i=0; i<500; i++) {
		for(j=0; j<500; j++)
			for(k=0; k<500; k++)
				c[i][j] += a[i][k] * b[k][j];
	}
	terminar=omp_get_wtime();
	printf("El tiempo de calculo neto es: %f\n", terminar-empezar);
}
