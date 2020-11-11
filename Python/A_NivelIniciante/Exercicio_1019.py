# -*- coding: utf-8 -*-

N = int(input())
horas = N/3600
minutos = (N - (horas * 3600))/60 
segundos = N -((horas * 3600) + (minutos * 60))
print("%s:%s:%s" %(str(horas),str(minutos),str(segundos)))