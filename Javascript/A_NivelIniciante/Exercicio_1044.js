var input = require("./readFile.js").input;
var lines = input.split('\n');
var line = lines[0].split(" ")
var a = line[0]*1
var b = line[1]*1
console.log(a>b? a%b==0?"Sao Multiplos" : "Nao sao Multiplos" : b%a==0?"Sao Multiplos":"Nao sao Multiplos" )