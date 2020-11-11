var input = require("./readFile.js").input;
function imprimir(grenais,vitoriaInter22,vitoriaGremio22,empates22){
    console.log(grenais + " grenais")
    console.log("Inter:" + vitoriaInter22);
    console.log("Gremio:" + vitoriaGremio22);
    console.log("Empates:" + empates22);
    if(vitoriaInter22>vitoriaGremio22){
        console.log("Inter venceu mais");
    }else if(vitoriaInter22<vitoriaGremio22){
        console.log("Gremio venceu mais"); 
    }else{
        console.log("Nao houve vencedor");
    }
        
}

var lines = input.split('\n');
var grenais = 1;
var empates = 0;
var vitoriasInter = 0;
var vitoriasGremio = 0;
var placar = lines.shift().split(" ");
var inter = parseInt(placar[0]);
var gremio = parseInt(placar[1]);
function quemGanhou(inter,gremio){
    if(inter==gremio){
        empate = empate+1;
    }else if(inter>gremio){
        vitoriasInter = vitoriasInter+1;
    }else{
        vitoriasGremio = vitoriasGremio+1;
    }
}

quemGanhou(inter,gremio);
console.log("Novo grenal (1-sim 2-nao)");
var continuar = parseInt(lines.shift());

if(continuar==1){
    while(continuar==1){

        if(continuar==1){
        grenais+=1;
        placar = lines.shift().split(" ");
        inter = parseInt(placar[0]);
        gremio = parseInt(placar[1]);
        quemGanhou(inter,gremio);
        console.log("Novo grenal (1-sim 2-nao)");
        continuar = parseInt(lines.shift());
        }
    }
    imprimir(grenais,vitoriasInter,vitoriasGremio,empates);
}else{
imprimir(grenais,vitoriasInter,vitoriasGremio,empates);
};


