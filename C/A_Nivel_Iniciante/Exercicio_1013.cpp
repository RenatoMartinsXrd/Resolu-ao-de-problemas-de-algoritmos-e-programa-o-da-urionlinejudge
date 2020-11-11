# include <stdio.h>

int main(){
	int a, b ,c,i,maior;
	scanf("%d %d %d",&a,&b,&c);
	int ns [3] = {a,b,c};
	maior =  ns[0];
	for(i =1;i<3;i++){
		if(ns[i]>maior){
			maior = ns[i];
		}
	}
	printf("%d eh o maior\n",maior);
	return 0;
}
