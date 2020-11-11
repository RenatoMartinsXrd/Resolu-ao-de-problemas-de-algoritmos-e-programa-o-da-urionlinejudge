# -*- coding: utf-8 -*-

def ache(lista,elemento):
    inicio = 0
    final = len(lista)-1
    achado=False
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
    
while True:
    try:
        sequencia = []
        saida = "N"
        leia = int(input())
        linha1 = input()
        linha1 = linha1.split(" ")
        numerotest = int(input())
        i = 0
        sequencia = linha1
        buscabinaria = ache(sequencia,numerotest)+1
       
        for y in range(1,int(leia)):
            if y>=2:
                if buscabinaria%y==0:                  
                    buscabinaria = 0
                    saida = "N"
                    break
                elif (buscabinaria -(buscabinaria//y))==y-1:
                   saida = "Y"
                   break
                else:  
                    buscabinaria = buscabinaria -(buscabinaria//y)
        print("%s" %saida)    
    except EOFError:
        break    