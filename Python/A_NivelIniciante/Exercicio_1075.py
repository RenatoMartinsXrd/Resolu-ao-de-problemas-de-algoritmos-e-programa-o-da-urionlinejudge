# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1075
y = int(input())
for x in range(1,10001):
    if x%y==2:
        print(x)


