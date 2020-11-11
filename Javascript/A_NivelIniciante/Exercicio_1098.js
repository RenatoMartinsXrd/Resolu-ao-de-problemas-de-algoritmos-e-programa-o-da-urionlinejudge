var i = 0
var j1 = 1
var j2 = 2
var j3 = 3
console.log("I="+i + " J=" + j1)  
console.log("I="+i + " J=" + j2)  
console.log("I="+i + " J=" + j3)  
for(let z =0;z<10;z++){
    if(z!=4 && z!=9 ){
        i+=0.2
        j1+=0.2
        j2+=0.2
        j3+=0.2
        console.log("I="+i.toFixed(1) + " J=" + j1.toFixed(1))
        console.log("I="+i.toFixed(1) + " J=" + j2.toFixed(1))  
        console.log("I="+i.toFixed(1) + " J=" + j3.toFixed(1))  
    }else{
        i+=0.2
        j1+=0.2
        j2+=0.2
        j3+=0.2
        console.log("I="+parseInt(i.toFixed(1)) + " J=" + parseInt(j1.toFixed(1)))
        console.log("I="+parseInt(i.toFixed(1))+ " J=" + parseInt(j2.toFixed(1)))  
        console.log("I="+parseInt(i.toFixed(1)) + " J=" + parseInt(j3.toFixed(1)))  
    }  
}
// 	i+=0.2
// 	j1+=0.2
// 	j2+=0.2
// 	j3+=0.2
// 	print("I=%.1f J=%.1f" %(i,j1))
// 	print("I=%.1f J=%.1f" %(i,j2))
// 	print("I=%.1f J=%.1f" %(i,j3))
// i+=0.2
// j1+=1
// j2+=0.2
// j3+=0.2
// print("I=%d J=%d" %(i,j1))
// print("I=%d J=%d" %(i,j2))
// print("I=%d J=%d" %(i,j3))
// j1-=0.8
// for x in range(4):
// 	i+=0.2
// 	j1+=0.2
// 	j2+=0.2
// 	j3+=0.2
// 	print("I=%.1f J=%.1f" %(i,j1))
// 	print("I=%.1f J=%.1f" %(i,j2))
// 	print("I=%.1f J=%.1f" %(i,j3))
// i+=1
// j1+=0.2
// j2+=0.2
// j3+=0.2
// print("I=%d J=%d" %(i,j1))
// print("I=%d J=%d" %(i,j2))
// print("I=%d J=%d" %(i,j3))