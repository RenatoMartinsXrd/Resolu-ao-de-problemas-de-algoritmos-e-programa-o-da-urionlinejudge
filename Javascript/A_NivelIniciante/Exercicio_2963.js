var input = require("./readFile.js").input;
var lines = input.split('\n');
var lengthLines = parseInt(lines.shift());
var maior = lines.shift();
var first = maior
var empates = 0;
var s = "S";
for(let i = 1;i<lengthLines;i++){
    if(first<lines[i]){
        console.log("N");
        s = "N"
        break;
    }
}
if(s=="S"){
    console.log("S")
}


