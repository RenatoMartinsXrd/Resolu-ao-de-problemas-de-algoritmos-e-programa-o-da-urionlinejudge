# -*- coding: utf-8 -*-

def primeiraPassada(palavra): 
    final = ""
    for x in palavra:
        if x.islower() or x.isupper(): 
            final+=chr(ord(x)+3) 
        else:
            final+=x
    return final
def segundaPassada(palavra):
    return palavra[::-1]
def terceiraPassada(palavra):
    metade = len(palavra)//2
    final = palavra[ : metade]
    palavra = palavra[metade :: ]
    for x in palavra:
        final+=chr(ord(x)-1)
    return final


qtd = int(input())
for x in range(qtd):
    text = input()
    print(terceiraPassada(segundaPassada(primeiraPassada(text))))
