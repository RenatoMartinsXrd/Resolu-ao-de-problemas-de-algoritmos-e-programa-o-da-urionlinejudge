# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1036
linha1 = input() 
A, B, C = linha1.split(" ")
A = float(A)
B = float(B)
C = float(C)
delta = ((B**2)-(4*A*C))
if(A!=0) and (delta > 0):
    print("R1 = %.5f" %((-(B) + (delta**(1/2)))/(2*A)))
    print("R2 = %.5f" %((-(B) - (delta**(1/2)))/(2*A)))
else:
    print("Impossivel calcular")
