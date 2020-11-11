while True:
	try:
		entrada = input().split()
		qtdPalavras = int(entrada[0])
		maxLinhas = int(entrada[1])
		maxCaractres = int(entrada[2])
		texto = input()
		linha = ""
		palavras = texto.split(" ")
		paginas = 0
		l = 0
		for x in range(len(palavras)):
			if(x!=0):
				pa = " " + palavras[x]
				temp = linha + " " + palavras[x]
			else:
				pa = linha + palavras[x]
				temp = linha + palavras[x]
			if(len(temp)>maxCaractres):
				linha = palavras[x] 
				l+=1
			else:
				linha+=pa
			if l == maxLinhas:
				paginas+=1
				l = 0
		l+=1
		if l == maxLinhas:
			paginas+=1
		elif l > 0:
			paginas+=1
		print(paginas)

	except EOFError:
		break

