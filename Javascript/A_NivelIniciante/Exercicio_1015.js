var input = require("./readFile.js").input;
var lines = input.split('\n');
var linha1 = lines.shift().split(" ");
x1 = linha1[0]
y1 = linha1[1]
var linha2 = lines.shift().split(" ");
x2 = linha2[0]
y2 = linha2[1]
var resultado = (parseFloat(x2)-parseFloat(x1))**2 + (parseFloat(y2)-parseFloat(y1))**2
console.log((resultado**(1/2)).toFixed(4));
