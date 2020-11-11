var input = require("./readFile.js").input;
var lines = input.split('\n');
console.log('DIFERENCA = ' + ((parseInt(lines.shift()) * parseInt(lines.shift())) - (parseInt(lines.shift()) * parseInt(lines.shift()))));