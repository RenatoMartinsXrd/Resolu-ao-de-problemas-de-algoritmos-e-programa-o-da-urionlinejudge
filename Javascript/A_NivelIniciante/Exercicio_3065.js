var input = require("./readFile.js").input;
var lines = input.split('\n');
var contador = 0
while(true){
contador+=1
var qtdNumeros = parseInt(lines.shift())
if(qtdNumeros==0){
    break;
}
var expressao = lines.shift() + "+"
var juntaNumero = ""
var total = 0
var sinalAnterior = "+"
function soma(i){
    total+=parseInt(juntaNumero)
    sinalAnterior = expressao[i]
    juntaNumero = ""    
}

function subtrair(i){
    total-=parseInt(juntaNumero)
    sinalAnterior = expressao[i]
    juntaNumero = ""     
}
for(let i = 0;i<expressao.length;i++){
    if(expressao[i]!="+" && expressao[i]!="-"){    
    juntaNumero+=expressao[i]
    }else if(sinalAnterior=="+"){
    soma(i)
    }else if(sinalAnterior=="-"){
    subtrair(i)
}
}
console.log("Teste " +  contador )
console.log(total)
console.log()
}