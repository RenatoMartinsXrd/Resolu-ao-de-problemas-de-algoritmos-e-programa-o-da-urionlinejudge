# -*- coding: cp1252 -*-
# -*- encoding: utf-8 -*-
#url do problema - https://www.urionlinejudge.com.br/judge/pt/problems/view/1020
dias = int(input())
anos = dias/365
meses = (dias -(anos * 365))/30
dias = dias -((anos * 365) + (meses * 30))
print("%d ano(s)" %anos)
print("%d mes(es)" %meses)
print("%d dia(s)" %dias)
