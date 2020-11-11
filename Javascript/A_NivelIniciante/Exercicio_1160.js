var input = require("./readFile.js").input;
var lines = input.split('\n');
for(let i = 1;i<=parseInt(lines[0]);i++){
var valores = lines[i].split(" ")
var CidadeA = parseInt(valores[0])
var CidadeB = parseInt(valores[1])
var taxaA = valores[2]/100
var taxaB = valores[3]/100
var anos = 0
while(CidadeA<=CidadeB && anos<=100){
    CidadeA += parseInt(CidadeA*taxaA)
    CidadeB += parseInt(CidadeB*taxaB)
    anos = anos+1  
}
if(anos>100){
    console.log("Mais de 1 seculo.")
}else{
    console.log(anos + " anos.")
}
}