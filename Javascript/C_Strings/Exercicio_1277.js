var input = require("./readFile.js").input;
var lines = input.split('\n');
var a = 1
for(let i = 1;i<=parseInt(lines[0]);i++){
    var n = lines[a]
    var vagabundos = ""
    a+=1
    var estudantes = lines[a].split(" ")
    a+=1
    var faltas = lines[a].trim().split(" ")
    a+=1
    var e = 0
    for(let falta of faltas){
    var total = falta.length
    var presencas = falta.match(RegExp("P", 'g')) || 0
    var atestados = falta.match(RegExp("M", 'g')) || 0
    var porcentagem = (presencas.length/(total - (atestados.length ||0))*100) || 0
    if(porcentagem<75){
    vagabundos+= estudantes[e] + " "
    }
    e+=1
    }
    console.log(vagabundos.trim())
}