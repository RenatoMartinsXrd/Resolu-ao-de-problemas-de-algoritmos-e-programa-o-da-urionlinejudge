var input = require("./readFile.js").input;
var lines = input.split('\n');
var value = parseFloat(lines.shift()).toFixed(2);
var cem = cinquenta =vinte = dez = cinco = dois = um = cincents = vintecincents = dezcents =cincocents=cents = 0
if(parseInt(value/100) >=1){
	cem = parseInt(value/100)
	value -= cem*100
}

value = parseFloat(value).toFixed(2)
if(parseInt(value/50) >=1){
	cinquenta = parseInt(value/50)
    value -= cinquenta*50
}
value = parseFloat(value).toFixed(2)
if(parseInt(value/20) >=1){
	vinte = parseInt(value/20.00)
    value -= vinte*20
}
value = parseFloat(value).toFixed(2)
if(parseInt(value/10) >= 1){
	dez = parseInt(value/10)
    value -= dez*10.00
}
value = parseFloat(value).toFixed(2)
if(parseInt(value/5) >= 1){
	cinco = parseInt(value/5)
    value -= cinco*5
}
value = parseFloat(value).toFixed(2)
if(parseInt(value/2) >= 1){
	dois = parseInt(value/2)
    value -= dois*2
}
value = parseFloat(value).toFixed(2)
if(parseInt(value/1) >= 1){
	um = parseInt(value/1)
    value -= um*1
}
value = parseFloat(value).toFixed(2)
if(parseInt(value/0.50) >= 1){
	cincents = parseInt(value/0.50)
    value -= cincents*0.50
}
value = parseFloat(value).toFixed(2)
if(parseInt(value/0.25) >= 1){
	vintecincents = parseInt(value/0.25)
    value -= vintecincents*0.25
}
value = parseFloat(value).toFixed(2)
if(parseInt(value/0.10) >= 1){
	dezcents = parseInt(value/0.10)
    value -= dezcents*0.10
}
value = parseFloat(value).toFixed(2)
if(parseInt(value/0.05) >= 1){
	cincocents = parseInt(value/0.05)
    value -= cincocents*0.05
}
value = parseFloat(value).toFixed(2)
if(parseInt(value/0.01) >= 0.998){
	cents = parseInt(value/0.01)
    value -= cents*0.01
}
console.log("NOTAS:")
console.log(cem + " nota(s) de R$ 100.00")
console.log(cinquenta + " nota(s) de R$ 50.00")
console.log(vinte + " nota(s) de R$ 20.00")
console.log(dez + " nota(s) de R$ 10.00")
console.log(cinco + " nota(s) de R$ 5.00")
console.log(dois + " nota(s) de R$ 2.00")
console.log("MOEDAS:")
console.log(um + " moeda(s) de R$ 1.00")
console.log(cincents + " moeda(s) de R$ 0.50")
console.log(vintecincents + " moeda(s) de R$ 0.25")
console.log(dezcents + " moeda(s) de R$ 0.10")
console.log(cincocents + " moeda(s) de R$ 0.05")
console.log(cents + " moeda(s) de R$ 0.01" )