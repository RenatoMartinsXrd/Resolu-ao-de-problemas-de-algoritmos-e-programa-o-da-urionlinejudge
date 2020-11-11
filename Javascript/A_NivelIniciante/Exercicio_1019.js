var input = require("./readFile.js").input;
var lines = input.split('\n');
var segundos = parseInt(lines.shift())
var h = segundos/3600
console.log(parseInt(h)+ ":" + parseInt((h - parseInt(h))*60) + ":" + parseInt(segundos%60))


