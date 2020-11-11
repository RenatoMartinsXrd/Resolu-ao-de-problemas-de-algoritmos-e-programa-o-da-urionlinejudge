# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1066
lista = []
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))

pares = 0
impares = 0
negativos = 0
positivos = 0
for x in lista:
    if(x%2 == 0):
        pares += 1
    else:#(x%2!=0):
        impares += 1
    if x!=0:
        if x<0:
            negativos += 1
        else:
            positivos += 1
print("%d valor(es) par(es)" %pares)
print("%d valor(es) impar(es)" %impares)
print("%d valor(es) positivo(s)" %positivos)
print("%d valor(es) negativo(s)" %negativos)
