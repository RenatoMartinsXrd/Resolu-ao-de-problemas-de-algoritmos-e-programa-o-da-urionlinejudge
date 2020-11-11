# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1070
leia = int(input())
x = leia
ac = 0
while ac!=6:
    if x %2!=0:
        print(x)
        ac = ac +1
    x = x + 1
