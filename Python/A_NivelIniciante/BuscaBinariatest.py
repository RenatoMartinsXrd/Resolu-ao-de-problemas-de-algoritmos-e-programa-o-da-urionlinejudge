# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
def ache(lista,elemento):
    inicio = 0
    final = len(lista)-1
    i = 0
    while inicio<=final:
        meio = (inicio+final)//2
        if int(lista[meio])==elemento:
            return meio
        elif elemento<int(lista[meio]):
            final = meio-1
        else:
            inicio = meio + 1
    return -1
lista = list(range(1,123,2))
print(lista)
print(ache(lista,57))
