var input = require("./readFile.js").input;
var lines = input.split('\n');
var linha = lines[0].split(" ")
var x = parseInt(linha[0])
var y = parseInt(linha[1])
var quotient = parseInt(Math.floor(x/y));
var remainder = x-(y*quotient);
if(y < 0){
    console.log(-quotient + " " + remainder) 
}else{
    console.log(quotient + " " + remainder)
}
