var input = require("./readFile.js").input;
var lines = input.split('\n');
var n = lines.shift()*1;
for(let i = 0;i<n;i++){
    var total1 = 0;
    var total2 = 0;
    for (let z = 0;z<3;z++){
    var lancamento = lines.shift().split(" ");
    total1+= lancamento[0]*1 * lancamento[1]*1;
    }
    for (let z = 0;z<3;z++){
    var lancamento = lines.shift().split(" ");
    total2+= lancamento[0]*1 * lancamento[1]*1 ;
    }
    console.log(total1>total2?"JOAO":"MARIA");
}