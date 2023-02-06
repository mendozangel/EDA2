/* Version serial */
#include <stdio.h>
#include <omp.h>

double prodpunto(double *a, double *b, int n) {
	double res=0;
	int i;
	
	#pragma omp parallel for reduction(+:res)
	for(i=0; i<n; i++) {
		res+= a[i]*b[i];
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