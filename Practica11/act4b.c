/* Version paralela con for */
#include <stdio.h>
#include <omp.h>
#define N 100000

int main (int argc, char *argv[]){
	
	double empezar, terminar;
	int i,j;
	float a[N], b[N], c[N], d[N], e[N], f[N];
	
    #pragma omp parallel
    {
        #pragma omp for
        for(i=0; i<N; i++)
		a[i] = b[i] = i*1.0;
	
        empezar=omp_get_wtime();
        
        #pragma omp for
        for(i=0; i<N; i++)
            c[i] = a[i]+b[i];
        
        #pragma omp for
        for(j=0; j<N; j++)
            d[j] = e[j]+f[j];
    }
	terminar=omp_get_wtime();
	printf("TIEMPO = %lf\n", empezar-terminar);
	return 0;
}
