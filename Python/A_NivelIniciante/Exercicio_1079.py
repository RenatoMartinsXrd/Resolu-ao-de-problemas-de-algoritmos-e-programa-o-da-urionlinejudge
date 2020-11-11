# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1079
y = int(input())
for x in range(y):
    linha1 = input()
    n1,n2,n3 = linha1.split()
    print("%.1f" %( ((float(n1)*2 )+(float(n2)*3) +(float(n3)*5))/10))
