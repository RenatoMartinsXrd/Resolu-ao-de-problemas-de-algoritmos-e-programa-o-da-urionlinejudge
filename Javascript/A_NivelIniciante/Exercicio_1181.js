var input = require("./readFile.js").input;
var lines = input.split('\n');
var linha = 2+(lines[0]*1)*12
var somaOuMedia = lines[1][0]
var soma = 0
for(let i = linha;i<linha+12;i++){
    soma+=parseFloat(lines[i])
}
console.log(somaOuMedia=="S"?soma : (soma/12).toFixed(1))