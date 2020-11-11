#include <stdio.h>
int main(){
	int n1,i;
	float kg;
	scanf("%i",&n1);
	for(i =0;i<n1;i++){
		scanf("%f",&kg);
		int dias = 0;
		while(kg>1){
			kg = kg/2;
			dias+=1;
		}
		printf("%i dias\n",dias);
	}
}
