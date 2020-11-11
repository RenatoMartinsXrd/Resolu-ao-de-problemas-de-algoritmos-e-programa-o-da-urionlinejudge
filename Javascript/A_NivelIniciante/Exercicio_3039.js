var input = require("./readFile.js").input;
var lines = input.split('\n');
var criancas = parseInt(lines.shift());
var m = 0
var f = 0

for(let i =0;i<criancas;i++){ 
if(lines[i].lastIndexOf("M")!=-1){
    m+=1
}else{
    f+=1
 }
}
console.log(m + " carrinhos")
console.log(f + " bonecas")



