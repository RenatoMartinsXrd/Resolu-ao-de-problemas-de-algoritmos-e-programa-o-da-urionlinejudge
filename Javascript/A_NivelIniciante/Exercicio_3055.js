var input = require("./readFile.js").input;
var lines = input.split('\n');
console.log(lines[1]*2 - lines[0])