var input = require("./readFile.js").input;
var lines = input.split('\n');

var entrada = parseInt(lines[0])
for(let i = 1;i<=entrada;i++){
    var string = lines[i].trim();
    var regex = new RegExp("[a-zA-Z]","g")
    var string2 = string.split("")
    while(a = regex.exec(string)){
        var letra = String.fromCharCode(string[a.index].charCodeAt(0)+3)
        string2[a.index] = letra
    }
    string = string2.reverse()
    
    for(let z = parseInt((string2.length)/2);z<string2.length;z++){
        let letra = String.fromCharCode(string2[z].charCodeAt(0)-1)
        string2[z] = letra
    }
    string = string2.join("")  
    console.log(string)
}


