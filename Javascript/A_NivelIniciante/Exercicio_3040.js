var input = require("./readFile.js").input;
var lines = input.split('\n');
var n = lines.shift()*1;
for(let i = 0;i<n;i++){
var arvore = lines.shift().split(" ");
console.log(arvore[0]*1>=200 && arvore[0]<=300 && arvore[1]*1>=50 && arvore[2]*1>=150?"Sim" : "Nao")    
}
