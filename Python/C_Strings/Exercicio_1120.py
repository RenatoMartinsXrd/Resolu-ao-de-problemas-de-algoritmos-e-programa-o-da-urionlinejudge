# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1120
while True:
    valores = ""
    valornovo= ""
    valores = input()
    teclafalha,valordigitado = valores.split()
    valornovo = valordigitado
    if teclafalha=="0" and valordigitado=="0":
        break
    for x in range(len(valordigitado)):
        if valordigitado[x] in teclafalha:
            valornovo = valordigitado.replace(valordigitado[x],"")
    if valornovo=="":
        valornovo = 0
    else:
        valornovo = int(valornovo)    
    print(valornovo)
        
