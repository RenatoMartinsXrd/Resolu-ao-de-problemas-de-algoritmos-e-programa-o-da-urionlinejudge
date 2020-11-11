# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1018
nota = int(input())
valores = [100,50,20,10,5,2,1]
print(nota)
for x in range(len(valores)):
    qtd = nota/valores[x]
    print("%d nota(s) de R$ %s,00" %(qtd,str(valores[x])))
    nota = nota - (valores[x]*int(qtd))
