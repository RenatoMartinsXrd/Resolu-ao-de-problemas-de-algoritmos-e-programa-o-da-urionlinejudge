var input = require("./readFile.js").input;
var lines = input.split('\n');
var eae = {"G":0,"V":0}
var a = parseInt(lines[0])
for(let i = 1;i<=a;i++){
	var fodase = lines[i].split(" ")
    eae[fodase[0].trim()] = (eae[fodase[0].trim()] || 0)+parseInt(fodase[1])
}
console.log(eae["G"]>eae["V"]?"NAO VAI TER CORTE, VAI TER LUTA!" : "A greve vai parar.")

