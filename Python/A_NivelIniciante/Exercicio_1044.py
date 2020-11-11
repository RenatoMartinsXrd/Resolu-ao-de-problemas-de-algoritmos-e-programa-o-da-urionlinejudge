# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1044
linha1 = raw_input()
A,B = linha1.split(" ")
A = int(A)
B = int(B)
if A%B==0 or B%A==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
   
