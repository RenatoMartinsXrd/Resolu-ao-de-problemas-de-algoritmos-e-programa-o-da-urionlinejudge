# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1021
nota = float(input()) + 0.00001
resultado = "NOTAS:\n"
valoresString = ["100.00","50.00","20.00","10.00","5.00","2.00","1.00","0.50","0.25","0.10","0.05","0.01"]
for x in range(len(valoresString)): 
    qtd = nota/float(valoresString[x])
    if x<=5:
        resultado+= "%d nota(s) de R$ %s\n" %(qtd,valoresString[x])
    elif x==6:
        resultado+="MOEDAS:\n"
    elif x>6 and x<len(valoresString)-1:
        resultado+= "%d moeda(s) de R$ %s\n" %(qtd,valoresString[x])
    elif x==len(valoresString)-1:
        resultado+= "%d moeda(s) de R$ %s" %(qtd,valoresString[x])
    nota = nota - (float(valoresString[x])*int(qtd))    
print(resultado)


