# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1078
y = int(input())
if(y > 2 and y<1000):
    for x in range(1,11):
        print("%d x %d = %d" %(x,y,x*y))
    
