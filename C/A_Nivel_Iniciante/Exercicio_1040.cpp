# include <stdio.h>
int main(){
	float n1,n2,n3,n4,nota_exame,media_final;
	scanf("%f %f %f %f",&n1,&n2,&n3,&n4);
	n1*=2;
	n2*=3;
	n3*=4;
	n4*=1;
	float media = (n1 + n2 + n3 + n4)/10.0;
	printf("Media: %.1f\n",media);
    if(media>=7){
		printf("Aluno aprovado.\n");
	}else if(media<5){
		printf("Aluno reprovado.\n");
	} 
    if(media>=5 && media<7){
    	printf("Aluno em exame.\n");
    	scanf("%f",&nota_exame);
    	printf("Nota do exame: %.1f\n",nota_exame);
    	media_final = (nota_exame + media)/2;
    	if(media>=5){
		printf("Aluno aprovado.\n");
		}else if(media<5){
			printf("Aluno reprovado.\n");
		}	 
    	printf("Media final: %.1f\n",media_final);
	}
	return 0;
}
