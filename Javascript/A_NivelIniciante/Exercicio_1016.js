var input = require("./readFile.js").input;
var lines = input.split('\n');
console.log((parseInt(lines.shift()) * 2) + " minutos");