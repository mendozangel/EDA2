/* Version paralela 1 */
#include <stdio.h>
#include <omp.h>

double prodpunto(double *a, double *b, int n) {
    int n_hilos = omp_get_num_threads();
	double res=0, resp[n_hilos];
	int i,tid,nth;
	#pragma omp parallel private (tid)
	{
		tid = omp_get_thread_num();
		resp[tid]=0;
		#pragma omp for
		for(i=0; i<n; i++){
			resp[tid]+=a[i]*b[i];
		}
		if(tid==0){
			nth = omp_get_num_threads();
			for(i=0; i<nth; i++){
				res+= resp[i];
			}
		}
	}
	return res;
}

int main() {
	double a[3] = {4,2,3};
	double b[3] = {2,1,5};
	double pp = prodpunto(a,b,4);
	printf("El producto punto de los arreglos a y b es : %lf\n",pp);
	return 0;
}