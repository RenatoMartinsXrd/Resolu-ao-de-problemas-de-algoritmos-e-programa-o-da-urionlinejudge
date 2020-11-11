var input = require("./readFile.js").input;
var lines = input.split('\n');

var proximo = parseFloat(lines.shift())
for(let i = 0;i<100;i++){
    console.log("N["+i+"] = " + proximo.toFixed(4))
    proximo = proximo/2.0
}


