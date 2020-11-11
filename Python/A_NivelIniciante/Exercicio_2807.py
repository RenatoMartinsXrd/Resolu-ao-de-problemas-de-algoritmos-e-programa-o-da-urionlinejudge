# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
qtd = int(input())
iccanobif = [1,1]
for x in range(1,qtd-1):
    iccanobif.append((iccanobif[x] + iccanobif[x-1]))
iccanobif.reverse()
if qtd!=1 or qtd!=1:
    print(' '.join(map(str, iccanobif)))
else:
    print(1)


