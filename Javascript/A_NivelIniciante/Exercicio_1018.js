var input = require("./readFile.js").input;
var lines = input.split('\n');
var notas = [100,50,20,10,5,2,1];
var valor = parseInt(lines.shift());
console.log(valor);
for(let i = 0;i<notas.length;i++){
let nota = notas[i]
let qtd = parseInt(valor/nota);
console.log(qtd + " nota(s) de R$ " + nota + ",00");
valor-=(nota*qtd);
}











// for x in range(len(valores)):
//     var qtd = nota/valores[x]
//     print("%d nota(s) de R$ %s,00" %(qtd,str(valores[x])))
//     nota = nota - (valores[x]*int(qtd))