entrada = input().split()
nAlunos = int(entrada[0]) + 1
nComputadores = int(entrada[1])
nQueimados = int(entrada[2])
nCompilador = int(entrada[3])

pcBom = nComputadores-(nQueimados+nCompilador)
if(pcBom<nAlunos):
	if nQueimados>(nCompilador//2):
		print("Caio, a culpa eh sua!")
	else:
		print("Igor bolado!")
else:
	print("Igor feliz!")