var input = require("./readFile.js").input;
var lines = input.split('\n');
var linha1 = lines[0].split(" ");
var cod_produto = parseFloat(linha1[0])
var qtd = parseFloat(linha1[1]);
var precos = [4.00,4.50,5.00,2.00,1.50];
console.log("Total: R$ " + (precos[cod_produto-1] * qtd).toFixed(2));