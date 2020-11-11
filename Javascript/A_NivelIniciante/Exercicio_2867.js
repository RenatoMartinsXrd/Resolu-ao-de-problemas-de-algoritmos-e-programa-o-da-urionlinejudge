var input = require("./readFile.js").input;
var lines = input.split('\n');
var n = lines.shift()*1
for(let i =0;i<n;i++){
    var linha = lines.shift().split(" ")
    var potencia = linha[0]**linha[1]
    var length = Math.log10(potencia) + 1 | 0;
    console.log(length);
}

