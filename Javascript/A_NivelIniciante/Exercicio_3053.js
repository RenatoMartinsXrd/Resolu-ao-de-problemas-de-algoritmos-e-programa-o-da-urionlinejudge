var input = require("./readFile.js").input;
var lines = input.split('\n');
var n = lines.shift()*1;
var atual = {"A":0,"B":0,"C":0};
var letra = lines.shift().trim();
atual[letra] = 1;

var local = letra ;
for(let x =0;x<n;x++){
	movimento = lines.shift()*1;
	if(atual["A"]==1){
        if (movimento==1){
            atual["B"]=1;
            atual["A"]=0;
            local = "B";
        }else if(movimento==2){
            continue;
        }else if(movimento==3){
            atual["C"]=1;
            atual["A"]=0;
            local = "C";
       }
    }else if(atual["B"]==1){
		if(movimento==1){
			atual["A"]=1;
			atual["B"]=0;
            local = "A";
        }else if(movimento==2){
			atual["C"]=1;
			atual["B"]=0;
            local = "C";
        }else if(movimento==3){
            continue;
        }
    }else if(atual["C"]==1){
		if(movimento==1){
            continue;
        }else if(movimento==2){
			atual["C"]=0;
			atual["B"]=1;
            local = "B";
        }else if(movimento==3){
			atual["C"]=0;
			atual["A"]=1;
            local = "A";
        }
    }
}
console.log(local);