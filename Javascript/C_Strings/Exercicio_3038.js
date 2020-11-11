var input = require("./readFile.js").input;
var lines = input.split('\n');
var dicionario = {"@":"a","&":"e","!":"i","*":"o","#":"u"}
var i = 0;
while(i<lines.length){
    var carta = lines[i]
	var newCarta = ""
    for(let z =0;z<carta.length;z++){
        newCarta+= dicionario[carta[z]] || carta[z]
    }
    console.log(newCarta)
    i=i+1
}



    



