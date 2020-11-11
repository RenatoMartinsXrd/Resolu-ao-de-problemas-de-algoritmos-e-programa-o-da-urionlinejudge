# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1037
A = float(input())          
if A<0 or A>100.0000:
    print("Fora do intervalo")
elif A>0 and A<=25.0000:
    print("Intervalo [0,25]")
elif A<=50.0000:
    print("Intervalo (25,50]")
elif A<=75.0000:
    print("Intervalo (50,75]")
elif A<=100.0000:
    print("Intervalo (75,100]")


