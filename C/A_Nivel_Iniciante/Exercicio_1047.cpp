# include <stdio.h>

int abs(int n){
	 return n < 0 ? (n * -1 ): n;
}

int main(){
	int hora_inicial, hora_final,minuto_inicial,minuto_final,inicio,final,res,resultado,hora,minuto;
	scanf("%d %d %d %d", &hora_inicial, &minuto_inicial, &hora_final, &minuto_final);
	hora_inicial *= 60;
	hora_final *= 60;
	
    inicio = hora_inicial + minuto_inicial;
    final = hora_final + minuto_final;
    res = final - inicio;

    if(hora_inicial==hora_final){
		res = (24*60);
		if(minuto_inicial>minuto_final){
			res -=(minuto_inicial - minuto_final);
        	hora = (res/60);
	        minuto = (res%60);
    	}else if(minuto_inicial<minuto_final){
			res = 0 + (minuto_final - minuto_inicial);
            hora = (res/60);
	        minuto = (res%60);
    	}else{
        	hora = (res/60);
	        minuto = (res%60);
    	}
	}else if(res>0){
    	    hora = (res/60);
	        minuto = (res%60);
	}else if(res<0){
		resultado = (24*60) - abs(res);
		hora = (resultado/60);
	    minuto = (resultado%60);
	}

    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n",hora,minuto);
    return 0;

}
