# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1021
nota = float(input())
valoresNotas = [100,50,20,10,5,2]
valoresMoedas = [1,0.50,0.25,0.10,0.05,0.01]
valoresNotasString = ["100.00","50.00","20.00","10.00","5.00","2.00"]
valoresMoedasString = ["1.00","0.50","0.25","0.10","0.05","0.01"]
print("NOTAS:")
for x in range(len(valoresNotas)):
    qtd = nota/valoresNotas[x]
    print("%d nota(s) de R$ %s" %(qtd,valoresNotasString[x]))
    nota = nota - (valoresNotas[x]*int(qtd))
print("MOEDAS:") 
for x in range(len(valoresMoedas)):
    qtd = nota/valoresMoedas[x]
    print("%d moeda(s) de R$ %s" %(qtd,valoresMoedasString[x]))
    nota = nota - (valoresMoedas[x]*int(qtd))
