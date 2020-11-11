# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1040
linha1 = raw_input()
A,B,C,D = linha1.split(" ")
A = float(A)*2
B = float(B)*3
C = float(C)*4
D = float(D)*1
Media = (A + B + C+D) / 10
print("Media: %.1f" %Media)
if Media>=7:
    print("Aluno aprovado.")
elif Media<5:
    print("Aluno reprovado.")
elif Media>=5 and Media<=6.9:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %.1f" %exame)
    mediadepoisexame = (Media+exame)/2
    if mediadepoisexame>=5:
        print("Aluno aprovado.")
    else:
        print("Aluno aprovado.")
    print("Media final: %.1f" %mediadepoisexame)    
        
