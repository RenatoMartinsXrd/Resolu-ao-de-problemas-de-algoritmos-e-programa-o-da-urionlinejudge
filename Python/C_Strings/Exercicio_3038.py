dicionario = {"@":"a","&":"e","!":"i","*":"o","#":"u"}
while(True):
	try:
		carta = input()
		newCarta = ""
		for letra in carta:
			newCarta+=dicionario.get(letra,letra)
		print(newCarta)
	except EOFError:
		break
