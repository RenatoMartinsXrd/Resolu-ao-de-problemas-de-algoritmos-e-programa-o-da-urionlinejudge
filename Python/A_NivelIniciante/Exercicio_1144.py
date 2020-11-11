# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1114

A = int(input())
for x in range(1,A+1):  
    print("%d %d %d" %(x,x*x,x*x**2))
    print("%d %d %d" %(x,(x*x)+1,(x*x**2)+1))
