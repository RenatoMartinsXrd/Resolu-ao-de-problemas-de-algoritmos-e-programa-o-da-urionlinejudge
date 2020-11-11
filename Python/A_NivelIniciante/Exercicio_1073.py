# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1073
leia = int(input())
aux = 1
for x in range(leia):   
    if aux%2==0:
        aux3 = aux**2
        print("%d^2 = %d" %(aux,aux3))
    aux = aux + 1
