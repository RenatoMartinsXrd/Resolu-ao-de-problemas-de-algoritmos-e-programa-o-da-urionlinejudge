var input = require("./readFile.js").input;
var lines = input.split('\n');
console.log(parseInt(lines[0]/365) + " ano(s)\n" + parseInt(lines[0]%365/30) + " mes(es)\n" + lines[0]%365%30 + " dia(s)")