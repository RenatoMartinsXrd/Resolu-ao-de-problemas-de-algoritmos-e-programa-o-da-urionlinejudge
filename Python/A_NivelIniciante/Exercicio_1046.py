# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1046
linha1 = raw_input()
hora_inicial,hora_final = linha1.split(" ")
hora_inicial = int(hora_inicial)
hora_final = int(hora_final)
duracao = 0
percorrer = 0
for x in range(1,24):
    hora_inicial = hora_inicial +1
    percorrer = hora_inicial
    duracao = duracao + 1
    if percorrer==hora_final:
        break;
    if percorrer==24:
        duracao = duracao + hora_final
        break
    if percorrer == 12:
        duracao = duracao + abs(hora_final-12)
        break 
print("O JOGO DUROU %d HORA(S)" %duracao)
