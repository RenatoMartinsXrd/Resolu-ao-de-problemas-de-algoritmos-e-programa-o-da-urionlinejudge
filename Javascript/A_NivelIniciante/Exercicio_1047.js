var input = require("./readFile.js").input;
var lines = input.split('\n');

var horas = lines[0].split(" ")
var hora_inicial = parseInt(horas[0]) * 60
var hora_final = parseInt(horas[2]) * 60
var minuto_inicial = parseInt(horas[1])
var minuto_final = parseInt(horas[3])

function convertMinutosEmHora(res){
	var hora = parseInt(res/60) 
	var minuto = parseInt(res%60) 
	return [hora,minuto]
}

function abs(n){
    return n < 0 ? n * -1 : n; 
}


var inicio = hora_inicial + minuto_inicial
var final = hora_final + minuto_final
var res = final - inicio

if(hora_inicial==hora_final){
	res = (24*60)
	if(minuto_inicial>minuto_final){
		res -=(minuto_inicial - minuto_final)
        horario = convertMinutosEmHora(res)
    }else if(minuto_inicial<minuto_final){
		res = 0 + (minuto_final - minuto_inicial)
        horario = convertMinutosEmHora(res)
    }else{
        horario = convertMinutosEmHora(res)
    }
}else if(res>0){
    horario = convertMinutosEmHora(res)
}else if(res<0){
	resultado = (24*60) - abs(res)
	horario = convertMinutosEmHora(resultado)
}

console.log("O JOGO DUROU "+ horario[0] + " HORA(S) E " + horario[1] + " MINUTO(S)");