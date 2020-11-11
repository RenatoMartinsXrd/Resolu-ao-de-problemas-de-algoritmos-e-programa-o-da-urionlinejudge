var input = require("./readFile.js").input;
var lines = input.split('\n');
var i = 1;
while(lines[i]){
    var kg = parseFloat(lines[i]);
    var dias=0;
    while(kg>1){
        kg = kg/2;
        dias= dias + 1;
    }
    console.log(dias + " dias")
    i+=1;
}