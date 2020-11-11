# -*- coding: utf-8 -*-
linha1 = input().split()
leia,amizadeNecessaria = linha1
runas = []
soma = 0
leia = int(leia)
amizadeNecessaria = int(amizadeNecessaria)
for x in range(leia):
    digitado = input().split()
    runas.append(digitado)
leia2 = int(input())
runasUsadas = input().split()
for z in range(leia2):
    letra = runasUsadas[z]
    for y in range(len(runas)):
        rona = runas[y]
        if rona[0] == letra:
            soma = soma + int(rona[1])
print(soma)
if soma<amizadeNecessaria:
    print("My precioooous")
else:
    print("You shall pass!")