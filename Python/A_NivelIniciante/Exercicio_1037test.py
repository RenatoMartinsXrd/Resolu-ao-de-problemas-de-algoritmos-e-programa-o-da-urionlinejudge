# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1037
a = float(input())
if  a>= 0 and a<= 25.0000:
    print("Intervalo [0,25]")
elif a>25.0000 and a<= 50.0000:
    print("Intervalo (25,50]")
elif a>50.0000 and a<= 75.0000:
    print("Intervalo (50,75]")
elif a>75.0000 and a<= 100.0000:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
