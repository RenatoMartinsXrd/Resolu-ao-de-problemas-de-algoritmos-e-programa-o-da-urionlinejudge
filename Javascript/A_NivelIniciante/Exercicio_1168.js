var input = require("./readFile.js").input;
var lines = input.split('\n');
var leia = lines.shift()*1
var leds = {"0":6,"1":2,"2":5,"3":5,"4":4,"5":5,"6":6,"7":3,"8":7,"9":6}
for(let i =0;i<leia;i++){
    var numeroleds = 0
    var valor = lines.shift()
    for(let z =0;z<valor.length;z++){
        numeroleds = numeroleds + leds[valor[z]]
    }
    console.log(numeroleds + " leds")
} 

