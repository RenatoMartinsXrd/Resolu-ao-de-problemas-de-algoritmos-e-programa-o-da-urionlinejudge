var input = require("./readFile.js").input;
var lines = input.split('\n');
var lines = lines[0].split(" ")
var a = lines[0]*1
var b = lines[1]*1
var c = lines[2]*1
if((a+b) > c && (a+c) > b && (c+b) > a){
    console.log("Perimetro = " + (a+b+c).toFixed(1))
}else{
    console.log("Area = " + ((a+b)/2 * c).toFixed(1))
}