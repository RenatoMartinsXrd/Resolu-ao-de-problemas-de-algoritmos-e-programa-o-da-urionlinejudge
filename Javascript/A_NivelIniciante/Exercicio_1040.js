var input = require("./readFile.js").input;
var lines = input.split('\n');
var lines2 = lines[0].split(" ");
var media = (lines2[0]*2 + lines2[1]*3 + lines2[2]*4 + lines2[3]*1)/10
console.log("Media: " + media.toFixed(1));
if(media>=7.0){
    console.log("Aluno aprovado.")
}else if(media<5.0){
    console.log("Aluno reprovado.")
}else if(media>=5.0 && media<=6.9){
    let exame= lines[1]*1
    console.log("Aluno em exame.");
    console.log("Nota do exame: " + exame.toFixed(1))
    var media_final = (exame + media)/2
    if(media_final>=5.0){
    console.log("Aluno aprovado.");
    }else{
    console.log("Aluno reprovado.");    
    }
    console.log("Media final: " + media_final.toFixed(1))
}