c = 1
while(True):
	entrada = input().split()
	if entrada[0] =="0" and entrada[1] =="0":
		break
	intervalos = []
	intervalo = input()
	intervalos.append(intervalo)
	a = 0
	for x in range(1,int(entrada[1])):
		g = intervalos[a].split(" ")
		inicio,fim = g[0],int(g[1])
		atual = input()
		inicio2 = atual.split(" ")[0]
		fim2 = atual.split(" ")[1]
		if int(fim2)>fim:
			if int(inicio2)>fim:
				a = a + 1
				intervalos.append(atual)
			else:
				intervalos[a] = inicio + " " + str(fim2)
	print("Teste %s" %str(c))
	for x in intervalos:
		print(x)
	c+=1
	print()
		


