alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u",
"v","w","x","y","z"]
t = int(input())
for x in range(t):
	maior = 0
	letraMaiores = ""
	frase = input().lower()
	for letra in alfabeto:
		contagem = frase.count(letra)
		if contagem>maior:
			maior = contagem
			letraMaiores = letra
		elif contagem==maior:
			letraMaiores+=letra
	print(letraMaiores)


