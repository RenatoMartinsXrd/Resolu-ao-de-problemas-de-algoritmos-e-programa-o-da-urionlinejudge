def contagem(qtdNumeros,salto):
	sequencia = {1:0}
	i = 0
	contador = 1
	for x in range(1,qtdNumeros):
		c = 0
		while(c<salto):
			i+=1
			if(i>qtdNumeros):
				i = 1
			if(i not in sequencia):
				c+=1
		contador+=1
		if(i==13 and contador<qtdNumeros):
			return False
		sequencia[i] = 0
	return True


def main():
	while(True):
		cidades = int(input())
		if(cidades==0):
			break
		x = 1
		while(True):
			if(contagem(cidades, x)==True):
				print("%d" %x)
				break
			x+=1
main()


