def ordenarVagoes(array):
	trocas = 0
	troca = True
	while(troca):
		troca = False
		for x in range(len(array)-1):
			element = int(array[x])
			nex = int(array[x+1])
			if element > nex:
				array[x] = nex
				array[x+1] = element
				trocas+=1
				troca = True
	return trocas



casos = int(input())
for x in range(casos):
	input()
	lista = input().split()
	print("Optimal train swapping takes %d swaps." %ordenarVagoes(lista))