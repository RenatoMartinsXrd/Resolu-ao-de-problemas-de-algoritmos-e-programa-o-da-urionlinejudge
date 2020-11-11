# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1045
linha1 = input()
A,B,C = linha1.split(" ")
A = float(A)
B = float(B)
C = float(C)
lista =[A,B,C]
listaSorted = sorted(lista,reverse=True)
A,B,C = listaSorted[0],listaSorted[1],listaSorted[2]
if A>=(B+C):
    print("NAO FORMA TRIANGULO")
else:
    if A**2 ==(B**2 + C**2):
        print("TRIANGULO RETANGULO")
    if A**2 >(B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")
    if A**2 <(B**2 + C**2):
        print("TRIANGULO ACUTANGULO")    
    if A==B==C:
        print("TRIANGULO EQUILATERO")
    elif A==B or A==C or B==C:
        print("TRIANGULO ISOSCELES")  
    
