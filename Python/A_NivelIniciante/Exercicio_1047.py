horas = input().split()
hora_inicial = int(horas[0]) * 60
hora_final = int(horas[2]) * 60
minuto_inicial = int(horas[1])
minuto_final = int(horas[3])

def convertMinutosEmHora(res):
	hora = (res//60) 
	minuto = (res%60)
	return [hora,minuto]

inicio = hora_inicial + minuto_inicial
final = hora_final + minuto_final
res = final - inicio



if(hora_inicial==hora_final):
	res = (24*60)
	if(minuto_inicial>minuto_final):
		res -=(minuto_inicial - minuto_final)
		horario = convertMinutosEmHora(res)
	elif(minuto_inicial<minuto_final):
		res = 0 + (minuto_final - minuto_inicial)
		horario = convertMinutosEmHora(res)
	else:
		horario = convertMinutosEmHora(res)
elif(res>0):
	horario = convertMinutosEmHora(res)
elif(res<0):
	resultado = (24*60) - abs(res)
	horario = convertMinutosEmHora(resultado)



print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(horario[0],horario[1]))