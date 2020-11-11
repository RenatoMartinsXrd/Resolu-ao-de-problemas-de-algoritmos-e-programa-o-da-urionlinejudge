var input = require("./readFile.js").input;
var lines = input.split('\n');
var line = lines[0].split(" ")
var lista =[line.shift()*1,line.shift()*1,line.shift()*1]
lista.sort((a, b)=>{return b-a});
var A = lista[0]
var B = lista[1]
var C = lista[2]
function rode(){
    if(A>=(B+C)){
        console.log("NAO FORMA TRIANGULO")
        return
    }
    if(A**2 ==(B**2 + C**2)){
        console.log("TRIANGULO RETANGULO")
    }
    if(A**2 >(B**2 + C**2)){
        console.log("TRIANGULO OBTUSANGULO")
    }
    if(A**2 <(B**2 + C**2)){
        console.log("TRIANGULO ACUTANGULO")    
    }
    if(A==B && A==C && B==C){
        console.log("TRIANGULO EQUILATERO")
    }else if(A==B || A==C || B==C){
        console.log("TRIANGULO ISOSCELES") 
    }
}
rode()

