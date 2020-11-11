var input = require("./readFile.js").input;
var lines = input.split('\n');
var c = 0
var media = 0
function nota(){
   var contador = 0
   while(contador!=2){
       var a = lines[c]*1
       if(a<0 || a>10){
           console.log("nota invalida")
           c+=1
       }else{
           media+=a
           c+=1
           contador+=1       
       }
   }
   console.log("media = " +(media/2).toFixed(2))
   media = 0
   contador = 0
   console.log("novo calculo (1-sim 2-nao)")
   calculo()
}
function calculo(){
    while(true){
        var a = lines[c]*1
        if(a==2){
            break
        }
        if(a == 1){
            c+=1
            nota()
        }else{
            console.log("novo calculo (1-sim 2-nao)")
            c+=1
        }
    }  
}
nota()


