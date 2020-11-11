var input = require("./readFile.js").input;
var lines = input.split('\n');
var conte = 0
while(true){
    var n = lines[conte]*1
    if(n==0){
        break
    }
    conte+=1
    var atualIndex = 1
    var qtdPolegada = 0
    var caminho = {"0": 0,"1":-1};
    for(let x = 0;x<n;x++){
        var linha = lines[conte]
        caminho["1"] = -1
        caminho[linha[0]] = 0
        caminho[linha[2]] = 1
        caminho[linha[4]] = 2
        if(caminho[1]!=-1){
            qtdPolegada+= Math.abs(atualIndex - caminho["0"])
            atualIndex = caminho["0"]
        }
        conte+=1
    }
    console.log(qtdPolegada)
    
}

