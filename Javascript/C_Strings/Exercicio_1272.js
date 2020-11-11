var input = require("./readFile.js").input;
var lines = input.split('\n');
z = parseInt(lines[0])
for(let i = 1;i<=z;i++){
    var a = lines[i].split(RegExp(" +"))
    s = ""
    for(var o of a){
        if(o){
            s+=o[0]
        }
    }
    console.log(s)
}