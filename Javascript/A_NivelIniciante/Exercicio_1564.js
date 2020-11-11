var input = require("./readFile.js").input;
var lines = input.split('\n');
while(lines.length > 0){
    let a = parseInt(lines.shift());
    if(a==0){
        console.log("vai ter copa!");
    }else if(a>0){
        console.log("vai ter duas!");
    }else{
        break;
    }
}
