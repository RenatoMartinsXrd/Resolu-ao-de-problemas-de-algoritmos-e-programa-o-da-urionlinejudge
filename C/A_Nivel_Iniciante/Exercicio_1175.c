#include <stdio.h>
#define INT 20
int main(){
	int i,aux;
	int x =0;
	int vetor[INT];
	for(i = 0;i<INT;i++){
		scanf("%i",&vetor[i]);
	}	
	   
	for(i = INT-1;i>=0;i--){
	printf("N[%i] = %i\n",x,vetor[i]);
	x++;
	}
	return 0;
}
