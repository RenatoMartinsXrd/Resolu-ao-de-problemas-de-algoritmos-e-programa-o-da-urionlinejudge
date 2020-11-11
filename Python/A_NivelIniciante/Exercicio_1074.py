# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1074
qtdRepeat = int(input())
for i in range(qtdRepeat):
    x = int(input())
    if x ==0:
        print("NULL")
    elif(x%2 == 0):
        if x>0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    else:
        if x>0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")
    

