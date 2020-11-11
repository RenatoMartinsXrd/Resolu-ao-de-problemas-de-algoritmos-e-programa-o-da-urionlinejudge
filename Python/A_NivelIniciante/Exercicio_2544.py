# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/2544

while True:
  try:
    clones = int(input())
    contador = 0
    x = 1
    if clones==1:
        print(contador)
    else:
        while x<clones:
            x = 2**contador
            contador = contador + 1
        print(contador-1)
  except EOFError:
    break
