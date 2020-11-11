var input = require("./readFile.js").input;
var lines = input.split('\n');
var line1 = lines.shift().split(" ");
var line2 = lines.shift().split(" ");
line1.shift();
line2.shift();
console.log("VALOR A PAGAR: R$ " + ((parseFloat(line1.shift()) * parseFloat(line1.shift())) + (parseFloat(line2.shift()) * parseFloat(line2.shift()))).toFixed(2));