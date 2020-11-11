var input = require("./readFile.js").input;
var lines = input.split('\n');
var i = 0;
var linha = lines[0].split(" ")
var n1 = parseInt(linha[0])
var n2 = parseInt(linha[1])
do{
    i = i + 1
    var soma = 0
    var s = ""
    if(n1>n2){
       for(let z = n2;z<=n1;z++){
           soma+=z
           s+= z.toString() + " "
       } 
    }else{
        for(let z = n1;z<=n2;z++){
            soma+=z
            s+= z.toString() + " "
        } 
    }
    s+= "Sum=" + soma.toString()
    console.log(s)
    linha = lines[i].split(" ")
    n1 = parseInt(linha[0])
    n2 = parseInt(linha[1])
}while(n1>0 && n2>0);