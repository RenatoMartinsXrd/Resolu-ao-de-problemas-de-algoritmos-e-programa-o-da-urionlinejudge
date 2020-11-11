# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1060
number = 0
for x in range(6):
    a = float(input())
    if a>=0:
        number = number +1
print("%d valores positivos" %number)
