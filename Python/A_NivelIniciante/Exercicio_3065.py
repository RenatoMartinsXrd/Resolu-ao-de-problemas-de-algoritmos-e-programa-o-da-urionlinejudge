# -*- coding: utf-8 -*-
contador = 0
while True:
    contador+=1
    qtd = int(input())
    if qtd==0:
        break
    expressao = input() + "+"
    juntaNumero = ""
    total = 0
    sinalAnterior = "+"
    for i in range(len(expressao)):
        if expressao[i]!="+" and expressao[i]!="-":
            juntaNumero+=expressao[i]
        elif sinalAnterior=="+":
            total+=int(juntaNumero)
            sinalAnterior = expressao[i]
            juntaNumero = ""    
        elif sinalAnterior=="-":
            total-=int(juntaNumero)
            sinalAnterior = expressao[i]
            juntaNumero = "" 
    print("Teste %d" %contador)
    print(total)
    print()