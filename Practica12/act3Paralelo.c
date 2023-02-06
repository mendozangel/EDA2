/* Version paralela */

#include <stdio.h>
#include <omp.h>

long fibonacci(int n) {
	long fn1, fn2, fn;
	int tid;
	if(n==0 || n== 1)
		return(n);
    if(n<30) {
        #pragma omp task shared(fn1) private(tid)
        {
			tid = omp_get_thread_num();
            fn1 = fibonacci(n-1);
			printf("Calculado desde el hilo: %d\n", tid);
        }
        #pragma omp task shared(fn2)
        {
			tid = omp_get_thread_num();
            fn2 = fibonacci(n-2);
			printf("Calculado desde el hilo: %d\n", tid);
        }
        #pragma omp taskwait
        {
            fn = fn1 + fn2;
        }
        return(fn);
	}
}

int main() {
	int nthr=0;
	int n;
	long resul;
	
	printf("\n Numero a calcular? ");
	scanf("%d", &n);
	
	#pragma omp parallel
	{
		#pragma omp single
		{
			resul = fibonacci(n);
		}
	}
	printf("\nEl numero Fibonacci de %2d es %ld\n",n,resul);
    return 0;
}


