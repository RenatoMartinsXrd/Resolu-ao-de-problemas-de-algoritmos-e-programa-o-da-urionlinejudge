var input = require("./readFile.js").input;
var lines = input.split('\n');
console.log('MEDIA = ' + ((parseFloat(lines.shift())*3.5+parseFloat(lines.shift())*7.5)/11).toFixed(5));