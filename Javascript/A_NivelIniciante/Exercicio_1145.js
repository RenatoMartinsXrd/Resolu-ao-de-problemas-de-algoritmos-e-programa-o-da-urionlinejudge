var input = require("./readFile.js").input;
var lines = input.split('\n');
var a = lines[0].split(" ")
var nLinhaFixed = parseInt(a[0])
var nLinhas = nLinhaFixed
var string = ""
for(let i = 1;i<=parseInt(a[1]);i++){
    string+=i + " "
    if(i==nLinhas){
        console.log(string.trim())
        string = ""
        nLinhas+=nLinhaFixed
    }
}

