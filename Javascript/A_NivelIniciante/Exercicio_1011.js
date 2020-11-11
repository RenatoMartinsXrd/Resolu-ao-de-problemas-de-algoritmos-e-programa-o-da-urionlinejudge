var input = require("./readFile.js").input;
var lines = input.split('\n');
console.log("VOLUME = " + ((4 * 3.14159 * parseFloat(lines.shift())**3)/3).toFixed(3));