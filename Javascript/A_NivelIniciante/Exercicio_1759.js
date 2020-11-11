var input = require("./readFile.js").input;
var lines = input.split('\n');
console.log(("Ho".padEnd((lines[0])*3," Ho")).trim() + "!") 