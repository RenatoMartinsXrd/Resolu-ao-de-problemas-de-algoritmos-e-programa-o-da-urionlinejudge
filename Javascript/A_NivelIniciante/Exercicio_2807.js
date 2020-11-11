var input = require("./readFile.js").input;
var lines = input.split('\n');
var qtd = parseInt(lines.shift());
var iccanobif = [1,1];
for(let i =1;i<qtd-1;i++){
    iccanobif.push((iccanobif[i] + iccanobif[i-1]));
}

if(qtd!=1 || qtd!=1){
    console.log(iccanobif.reverse().join(" "));
}else{
    console.log(1)
}

