# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1051
Renda = float(input())

if Renda>0 and Renda<=2000:
    print("Isento")
elif Renda>2000 and Renda<=3000:
    renda1 = Renda - 2000
    print("R$ %.2f" %(renda1 * 0.08))
elif Renda>3000 and Renda<=4500:
    renda2 = Renda - 3000
    print("R$ %.2f" %(((Renda - 3000) *0.18) + 80))
else:
    print("R$ %.2f" %(((Renda - 4500) *0.28) + 270 + 80))

