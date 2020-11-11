# -*- coding: utf-8 -*-
def binarySearchLinear(A, item):
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio] == item:
            while(meio!=0 and A[meio-1] == item):
                meio-=1
            return str(item) +" found at " + str(meio+1)
       
        elif A[meio] > item:
            direita = meio - 1
        else: 
            esquerda = meio + 1
    return str(item) + " not found"


def mergeSort(lista):

    if len(lista) > 1:

        meio = len(lista)//2
        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]

        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):

            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1

        while i < len(listaDaEsquerda):

            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1
    return lista

c = 1
while True:
    entrada = input().split(" ")
    marmores = int(entrada[0])
    consulta = int(entrada[1])
    array = []
    if(marmores == 0 and consulta==0):
        break
    for x in range(marmores):
        marmore = int(input())
        array.append(marmore)
    array = mergeSort(array)
    print("CASE# %d:" %c)
    for z in range(consulta):
        consulte = int(input())
        print(binarySearchLinear(array, consulte))
    c+=1