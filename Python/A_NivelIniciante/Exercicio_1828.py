qtd = int(input())
possibilidades = {"pedra": {"papel":1,"tesoura":0,"lagarto":0,"Spock":1,"pedra":2},
"papel":{"papel":2,"tesoura":1,"lagarto":1,"Spock":0,"pedra":0}
,"tesoura":{"papel":0,"tesoura":2,"lagarto":0,"Spock":1,"pedra":1},
"lagarto":{"papel":0,"tesoura":1,"lagarto":2,"Spock":0,"pedra":1},
"Spock":{"papel":1,"tesoura":0,"lagarto":1,"Spock":2,"pedra":0}}
c = 1
for x in range(qtd):
	jg1,jg2 = input().split(" ")
	resultado = possibilidades[jg1][jg2]
	if resultado==0:
		print("Caso #%d: Bazinga!" %c)
	elif resultado==1:
		print("Caso #%d: Raj trapaceou!" %c)
	else:
		print("Caso #%d: De novo!" %c)
	c+=1
