/* Version serial */

#include <stdio.h>

long fibonacci(int n) {
	long fn1, fn2, fn;
    int id;

    if(n==0 || n==1)
        return(n);

    if(n<30) {
        fn1 = fibonacci(n-1);
        fn2 = fibonacci(n-2);
        fn = fn1+fn2;
    }
        return(fn);
}

int main() {
	int nthr=0;
	int n;
	long resul;
	
	printf("\n Numero a calcular? ");
	scanf("%d", &n);

	resul = fibonacci(n);
	printf("\nEl numero Fibonacci de %2d es %ld\n",n,resul);
    return 0;
}

