# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1035
linha1 = input() 
A, B, C ,D = linha1.split(" ")
A = int(A)
B = int(B)
C = int(C)
D = int(D)
if B>C and D>A and C+D>A+B and C>0 and D>0 and A%2==0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

