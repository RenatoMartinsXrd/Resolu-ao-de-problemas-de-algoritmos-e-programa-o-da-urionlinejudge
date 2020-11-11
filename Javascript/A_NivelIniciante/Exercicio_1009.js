var input = require("./readFile.js").input;
var lines = input.split('\n');
lines.shift();
var salario = parseFloat(lines.shift());
var venda = parseFloat(lines.shift());
console.log("TOTAL = R$ " + (salario +(venda*0.15)).toFixed(2));