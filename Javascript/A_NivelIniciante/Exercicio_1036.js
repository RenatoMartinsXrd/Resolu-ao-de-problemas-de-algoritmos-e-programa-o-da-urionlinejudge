var input = require("./readFile.js").input;
var lines = input.split('\n');
lines = lines[0].split(" ");
A = lines[0];
B = lines[1];
C = lines[2];
var delta = ((B**2)-(4*A*C))
console.log(delta)
if((A!=0) && (delta > 0)){
    console.log("R1 = " + ((-(B) + (delta**(1/2)))/(2*A)).toFixed(5))
    console.log("R2 = " + ((-(B) - (delta**(1/2)))/(2*A)).toFixed(5))
}else{
    console.log("Impossivel calcular")
}
 