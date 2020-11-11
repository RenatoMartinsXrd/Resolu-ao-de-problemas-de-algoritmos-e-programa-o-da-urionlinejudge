var input = require("./readFile.js").input;
var lines = input.split('\n');
var meses = {"1" : "January","2":"February","3":"March","4":"April","5":"May","6":"June","7":"July","8":"August","9":"September","10":"October","11":"November","12":"December"}
// var meses = ["January","February","March","April","May","June","July","August","September","October","November","December"]
console.log(meses[lines[0].trim()] || 0)
console.log(meses[parseInt(lines[0])-1])