var input = require("./readFile.js").input;
var lines = input.split('\n');
var linha1 = lines[0].split(" ");
var x = linha1[0]*1;
var y = linha1[1]*1;
if(x>0 && y>0){
console.log("Q1");
}else if(x==0 && y==0){
console.log("Origem");
}else if(x<0 && y>0){
console.log("Q2");
}else if(x<0 && y<0){
console.log("Q3");
}else if(x>0 && y<0){
console.log("Q4");    
}else if(x==0 && y<0 || y>0){
console.log("Eixo Y");
}else if(y==0 && x<0 || x>0){
console.log("Eixo X");    
}