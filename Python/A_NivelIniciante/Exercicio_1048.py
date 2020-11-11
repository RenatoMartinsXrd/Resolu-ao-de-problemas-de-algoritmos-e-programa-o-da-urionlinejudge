# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1048
A = float(input())
porcentagem = 0
reajuste = 0.0
novosalario = 0.0
class salario():
    def __init__(self,A,porcentagemDecimal,porcentagem,reajuste,novosalario):
        self.novosalario = A*((porcentagemDecimal/100)+1)
        self.reajuste = (float(porcentagemDecimal)/100)*A
        self.porcentagem = porcentagemDecimal
if A>0 and A<=400:
    pessoa = salario(A,15,porcentagem,reajuste,novosalario)
elif A>400 and A<=800:
    pessoa = salario(A,12,porcentagem,reajuste,novosalario)
elif A>800 and A<=1200:
    pessoa = salario(A,10,porcentagem,reajuste,novosalario)
elif A>1200 and A<=2000:
    pessoa = salario(A,7,porcentagem,reajuste,novosalario)
elif A>2000:
    pessoa = salario(A,4,porcentagem,reajuste,novosalario)
print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %d %%" %(pessoa.novosalario,pessoa.reajuste,pessoa.porcentagem))   
