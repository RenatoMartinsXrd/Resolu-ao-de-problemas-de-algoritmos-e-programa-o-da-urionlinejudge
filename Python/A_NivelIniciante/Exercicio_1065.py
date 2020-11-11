# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1065
qtdPar = 0
for x in range(5):
    a = int(input())
    if a%2==0:
        qtdPar = qtdPar + 1
print("%d valores pares" %qtdPar)
