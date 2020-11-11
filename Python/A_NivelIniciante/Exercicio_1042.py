# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1042
linha1 = raw_input()
lista = list()
A,B,C = linha1.split(" ")
lista = [int(A),int(B),int(C)]
listaSorted = sorted(lista)
for x in range(3):
    print(listaSorted[x])
print("")
for y in range(3):
    print(lista[y])
