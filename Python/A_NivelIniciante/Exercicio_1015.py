# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1015
linha1 = input().split(" ")
linha2 = input().split(" ")
x1, y1 = linha1
x2, y2 = linha2
resultado = (float(x2)-float(x1))**2 + (float(y2)-float(y1))**2
print("%.4f" %(resultado**(1/2)))
