while True:
	try:
		processos = input()
		maxCiclo = int(input())
		ciclos = 0
		qtdSubCiclos = 0
		for x in processos:
			if x=="W":
				ciclos+=1
				qtdSubCiclos = 0
			elif x=="R" and qtdSubCiclos==0:
				ciclos+=1
				qtdSubCiclos+=1	
			elif x=="R" and qtdSubCiclos<maxCiclo:
				qtdSubCiclos+=1	
			if x=="R" and qtdSubCiclos>=maxCiclo:
				qtdSubCiclos = 0
		print(ciclos)
	except EOFError:
		break