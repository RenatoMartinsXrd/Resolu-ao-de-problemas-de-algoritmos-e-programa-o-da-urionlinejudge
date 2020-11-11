var input = require("./readFile.js").input;
var lines = input.split('\n');
var a = parseFloat(lines.shift())
if(a<0 || a>100){
    console.log("Fora de intervalo")
}else if(a>=0 && a<=25){
    console.log("Intervalo [0,25]");
}else if(a<=50){
    console.log("Intervalo (25,50]");
}else if(a<=75){
    console.log("Intervalo (50,75]")
}else if(a<=100){
    console.log("Intervalo (75,100]")
}