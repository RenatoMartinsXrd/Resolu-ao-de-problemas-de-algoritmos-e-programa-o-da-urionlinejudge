var input = require("./readFile.js").input;
var lines = input.split('\n');
var lista = ["PROXYCITY","P.Y.N.G.","DNSUEY!","SERVERS","HOST!","CRIPTONIZE","OFFLINE DAY","SALT","ANSWER!","RAR?","WIFI ANTENNAS"]
let aux = parseInt(lines.shift());
for(let i = 0;i<aux;i++){
    let botoes = lines.shift().split(" ");
    let A = parseInt(botoes[0]);
    let B = parseInt(botoes[1]); 
    console.log(lista[(A+B)]);
}
