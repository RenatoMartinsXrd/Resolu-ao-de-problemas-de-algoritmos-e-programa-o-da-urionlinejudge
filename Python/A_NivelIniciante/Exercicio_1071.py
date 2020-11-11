# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1071
X = int(input())
Y = int(input())

soma = 0
for x in range((Y +1),X):
    if x%2!=0:
        soma = soma + x
print(soma)
