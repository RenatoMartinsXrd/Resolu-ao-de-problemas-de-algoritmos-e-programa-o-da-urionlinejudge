var antes = Date.now();
var input = require("./readFile.js").input;
var lines = input.split('\n');
lines = lines.shift().split(" ");
var atual = lines.shift();
    for(let i =0;i<2;i++){
        if(parseInt(lines[i])>atual){
            atual = parseInt(lines[i]);
           }
    }
console.log(atual + " eh o maior");      
var duracao = Date.now() - antes;
console.log("levou " + duracao + "ms");