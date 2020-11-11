# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1041
linha1 = raw_input()
x,y = linha1.split(" ")
x = float(x)
y = float(y)
if x>0 and y>0:
    print("Q1")
elif x==0 and y==0:
    print("Origem")
elif x<0 and y>0:
    print("Q2")
elif x<0 and y<0:
    print("Q3")
elif x>0 and y<0:
    print("Q4")      
elif x==0 and y<0 or y>0:
    print("Eixo Y")
elif y==0 and x<0 or x>0:
    print("Eixo X")    
