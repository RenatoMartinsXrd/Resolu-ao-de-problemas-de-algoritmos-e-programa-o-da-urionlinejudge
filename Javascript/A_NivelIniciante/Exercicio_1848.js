var input = require("./readFile.js").input;
var lines = input.split('\n');
var caw = 0;
var soma = 0;

function covertaByDecimal(num){
var resultado = 0;
var cont = num.length;
for(let i= 0;i<num.length;i++){
    cont = cont - 1
    if(num[cont]==0){
    continue;
    }else{
        resultado+=(2**i);
    }
}
return resultado;
}

while(caw<3){
var entrada = lines.shift();
var binario = "";
if(entrada.match("caw caw")==null){
entrada[0]=="-"?binario+="0":binario+="1";
entrada[1]=="-"?binario+="0":binario+="1";
entrada[2]=="-"?binario+="0":binario+="1";
soma+=covertaByDecimal(binario);
}else{
    console.log(soma)
    soma = 0;
    caw+=1;
}
}