# include <stdio.h>
int menorSalto(int qtdCidades){
	int [qtdCidades] cidadesEliminadas;
	int c = 0;
	for(int i = 1;i<qtdCidades;i++){
		for(int z = i;z<qtdCidades;z+=i){
			if(z==13 && i!=qtdCidades){
				break;
			}else{
			cidadesEliminadas[c] = z;
			c++;	
			}
	    }
	}
}

int main(){
	while(true){
		int cidades;
		scanf("%i",&entrada);
		if(cidades==0){
			break;
		}
		prinf("%i",menorSalto(cidades))
	}
	return 0;
}
