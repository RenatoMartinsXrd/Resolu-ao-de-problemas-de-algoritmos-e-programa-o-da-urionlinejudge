# -*- coding: utf-8 -*-

#formula (a + b + abs(a-b))/2
#Com este codigo podemos comparar quantos for necessario
lis = maior = list()
i,quantosequer = 0,3
linha1 = input().split(" ")
for x in range(quantosequer):
    lis.append(float(linha1[x]))
    if x==1:
        maior.append((lis[x]+ lis[0] + abs(lis[x] - lis[0]))/2)
    elif x>1:
        ultimo = maior.pop(-1)
        maior.append((lis[x] + ultimo + abs(ultimo - lis[x]))/2)
        i = i + 1
print("%d eh o maior" %maior.pop(-1))