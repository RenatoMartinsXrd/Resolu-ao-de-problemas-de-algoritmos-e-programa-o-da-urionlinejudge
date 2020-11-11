# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1064

positivos = 0
media = 0
for x in range(6):
    A = float(input())
    if A>0:
        positivos = positivos + 1
        media = (media + A)
print("%d valores positivos\n%.1f"%(positivos,float(media/positivos)))
