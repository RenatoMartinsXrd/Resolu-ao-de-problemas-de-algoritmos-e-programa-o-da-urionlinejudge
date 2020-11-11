var input = require("./readFile.js").input;
var lines = input.split('\n');
console.log( ( parseFloat(lines.shift())/parseFloat(lines.shift())).toFixed(3) + " km/l");