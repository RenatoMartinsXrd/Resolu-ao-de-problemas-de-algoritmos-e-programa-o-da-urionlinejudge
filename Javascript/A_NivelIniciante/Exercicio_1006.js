var input = require("./readFile.js").input;
var lines = input.split('\n');
console.log('MEDIA = ' + ((parseFloat(lines.shift())*2+parseFloat(lines.shift())*3 + parseFloat(lines.shift())*5)/10).toFixed(1));