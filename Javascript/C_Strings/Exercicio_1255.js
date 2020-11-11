var input = require("./readFile.js").input;
var lines = input.split('\n');
var n = lines.shift();
for(let i =0;i<parseInt(n);i++){
    var alfabeto = new Map([["a", 0], ["b", 0], ["c", 0],
["a", 0], ["b", 0], ["c", 0],
["d", 0], ["e", 0], ["f", 0],
["g", 0], ["h", 0], ["i", 0],
["j", 0], ["k", 0], ["l", 0],
["m", 0], ["n", 0], ["o", 0],
["p", 0], ["q", 0], ["r", 0],
["s", 0], ["t", 0], ["u", 0],
["v", 0], ["w", 0], ["x", 0],
["y", 0], ["z", 0]
]);
    let string = lines[i];
    var chaves = Array.from(alfabeto.keys())
    let firstMaiorNumero = 0
    let firstMaiorLetra = ""
    let empates = ""
    for(let i =0;i<chaves.length;i++){
    var regexp = new RegExp(`${chaves[i]}`, "gi");
    let ache = string.match(regexp)
    if(ache!=null){
        let tam = ache.length
        let letra = chaves[i]
        alfabeto.set(letra,tam)
        if(i==0){
            firstMaiorNumero = tam
            empates+=letra
        }else{
            if(tam==firstMaiorNumero){
            empates+=letra
            }else if(tam>firstMaiorNumero){
                firstMaiorNumero = tam
                empates = letra
            }
        }
    }
    
    }
    console.log(empates)
}





// sayings.set("d",2);
// console.log(sayings.get("d"))