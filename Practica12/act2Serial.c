/* Versión serial*/
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int NG = 256, N =1000;
double empezar, terminar;

int main() {
	int i,j;
	int histo[NG], IMA[N][N];
	
	for(i=0; i<N; i++) {
		for(j=0; j<N; j++){
			IMA[i][j] = rand() % (NG+1);
		}
	}
	for(i=0; i<NG; i++)
		histo[i] = 0;
	empezar = omp_get_wtime();
	for(i=0; i<N; i++) {
		for(j=0; j<N; j++){
			histo[IMA[i][j]]++;
		}
	}
	terminar = omp_get_wtime();
	printf("El tiempo de calculo neto es: %lf\n", terminar-empezar);
}
