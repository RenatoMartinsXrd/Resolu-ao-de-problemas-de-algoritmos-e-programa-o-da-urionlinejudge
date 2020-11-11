var input = require("./readFile.js").input;
var lines = input.split('\n');

function fatorial(n){
    if(n==0 || n==1) return 1;
    return n * fatorial(n-1)
}
console.log(fatorial(lines[0]*1))