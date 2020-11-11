var input = require("./readFile.js").input;
var lines = input.split('\n');
while(true){
    var pares = 0
    var myMap = new Map();
    var n = lines.shift()*1
    var a = ""
    for(let z = 0;z<n;z++){
        var line = lines.shift().split(" ");
        var numeroBota = line[0]*1
        
        if(myMap.has(numeroBota)){
        a = myMap.get(numeroBota)+line[1].trim()
        myMap.set(numeroBota,a);
        continue;
        }
        myMap.set(numeroBota,line[1].trim());
        
    }

    myMap.forEach((value)=>
    {  
        var D = 0
        var E = 0
        if(value.match(/D/g)!=null){
            D = value.match(/D/g).length
        }
        if(value.match(/E/g)!=null){
            E = value.match(/E/g).length;
        }
        if(D>E && E!=0){
            pares+=E
        }else if(E>D && D!=0){
           pares+=D
        }else if(E==D){
            pares+=E
        }
    });
     console.log(pares)
     if(lines.length==0){
         break;
     }
}

