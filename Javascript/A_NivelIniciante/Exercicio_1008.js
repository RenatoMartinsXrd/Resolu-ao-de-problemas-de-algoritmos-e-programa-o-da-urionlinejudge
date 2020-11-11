var input = require("./readFile.js").input;
var lines = input.split('\n');
console.log("NUMBER = " + lines.shift());
console.log("SALARY = U$ " + (parseFloat(lines.shift()) * parseFloat(lines.shift())).toFixed(2));