var input = require("./readFile.js").input;
var lines = input.split('\n');
var N = parseInt(lines[0])
console.log(((N+1)*(N+2))/2)