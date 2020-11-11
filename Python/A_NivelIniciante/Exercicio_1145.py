# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1145
linha1 = input()
X,Y = linha1.split()
X = int(X)
Y = int(Y)
nLinha = X
resultado = ""
for x in range(1,Y+1):
    resultado += str(x) + " "
    if x==nLinha:
    	print(resultado.strip())
    	resultado = ""
    	nLinha+=X



