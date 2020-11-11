var input = require("./readFile.js").input;
var lines = input.split('\n');
var saida = ""
var contador =0
var qtdLoop= 2
var conta = 0
while(qtdLoop!=0){
    var saida = ""
    qtdLoop = parseInt(lines[conta]);
    

    for(let i =0;i<qtdLoop;i++){
        conta+=1
        if(i!=(qtdLoop-1)){
            saida += lines[conta].trim().replace(/\s{1,}/g, ' ')+ "\n";
        }else{
            saida += lines[conta].trim().replace(/\s{1,}/g, ' ');
        }
    }
    var saidaArray = saida.split("\n");
    var linha = saida.split("\n");
    var atualString = linha[0];
    var atualIndex = 0;
    var tamanhos = []
    for(let i =1;i<linha.length;i++){
            if(linha[i].length>atualString.length){
                atualString = linha[i];
                atualIndex = i;
            }
    }
    var saidaFinal = ""
    for(let i =0;i<linha.length;i++){
        let espacos = atualString.length - linha[i].length;
        let stringespaco = ""
        for(let i = 0;i<espacos;i++){
            stringespaco +=" "
        }
        if(i!=(linha.length-1)){
            saidaFinal+= ((stringespaco+=saidaArray[i]+"\n"))
        }else{
            saidaFinal+= (stringespaco+=saidaArray[i]);
        }
        
    }
    if(qtdLoop!=0){
        if(contador!=0){
            console.log("")
            console.log(saidaFinal.trimRight());
        }else{
            console.log(saidaFinal.trimRight());
        }

    }
    contador+=1
    conta+=1
}



