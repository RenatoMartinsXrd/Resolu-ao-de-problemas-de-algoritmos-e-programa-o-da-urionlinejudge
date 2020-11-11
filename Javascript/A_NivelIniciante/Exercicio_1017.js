var input = require("./readFile.js").input;
var lines = input.split('\n');
console.log(((parseInt(lines.shift()) / 12.0)* parseInt(lines.shift())).toFixed(3));