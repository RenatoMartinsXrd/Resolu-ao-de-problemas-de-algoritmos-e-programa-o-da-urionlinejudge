var input = require("./readFile.js").input;
var lines = input.split('\n');
console.log('PROD = ' + (parseInt(lines.shift())*parseInt(lines.shift())));