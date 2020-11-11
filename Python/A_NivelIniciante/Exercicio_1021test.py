# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
nota = float(input())
valores = [100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01]
valoresString = ["100.00","50.00","20.00","10.00","5.00","2.00","1.00","0.50","0.25","0.10","0.05","0.01"]
for x in range(len(valores)):
    qtd = nota/valores[x]+0.00001
    if x<=5:
        if x==0:
            print("NOTAS:")
        print("{} nota(s) de R$ {}".format(str(int(qtd)),valoresString[x]))
    else:
        if x==6:
            print("MOEDAS:")
        print("{} moedas(s) de R$ {}".format(str(int(qtd)),valoresString[x]))
    nota = nota - (valores[x]*int(qtd))
    
