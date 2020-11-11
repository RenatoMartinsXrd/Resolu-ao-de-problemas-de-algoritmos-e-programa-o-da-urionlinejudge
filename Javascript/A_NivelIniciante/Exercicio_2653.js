var input = require("./readFile.js").input;
var lines = input.split('\n');
var joias = new Set();
var tam = lines.length;
for(let i =0;i<tam-1;i++){
    joias.add(lines.shift());   
}
console.log(joias.size);





