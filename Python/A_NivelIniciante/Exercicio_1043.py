# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1043
linha1 = raw_input()
A,B,C = linha1.split(" ")
A = float(A)
B = float(B)
C = float(C)
def testador(lado):
    if (B - C)<lado<B + C:
    	return True
    return False
if testador(A)==True:
    print("Perimetro = %.1f" %(A+B+C))
else:
    print("Area = %.1f" %((A+B)/2 * C))
    
