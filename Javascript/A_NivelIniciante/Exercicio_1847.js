var input = require("./readFile.js").input;
var lines = input.split('\n');
var linha= lines[0].split(" ")
var A = parseInt(linha[0])
var B = parseInt(linha[1])
var C = parseInt(linha[2])
if(B<A){
	if(C>=B){
        console.log(":)");
    }else{
		let dia4 = A - B
		let dia5 = B - C
		if(dia5<dia4){
            console.log(":)");
        }else{
            console.log(":(");
        }
    }

}else if(B>A){
	if(C<=B){
        console.log(":(");
    }else{
		let dia1 = B - A
		let dia2 = C - B
		if(dia2<dia1){
            console.log(":(");
        }else{
            console.log(":)");
        }
    }
}else if(A==B && C>B){
    console.log(":)");
}else{
    console.log(":(");
}
