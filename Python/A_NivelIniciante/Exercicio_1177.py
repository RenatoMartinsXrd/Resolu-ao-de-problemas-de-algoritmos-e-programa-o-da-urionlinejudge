def preenche(vet,tamanhoVet,inicio,fim,contador):
	if contador==tamanhoVet:
		return vet
	vet.append(inicio)
	if inicio==fim:
		inicio = 0
	print("N[%i] = %i" %(contador,inicio))
	preenche(vet, tamanhoVet, inicio+1, fim,contador+1)

def main():
	vet = []
	T = int(input())
	preenche(vet, 1000, 0, T,0)
main()


# vet = []
# T = int(input())
# i = 0
# for x in range(1000):
# 	vet.append(i)
# 	i+=1
# 	if(i==T):
# 		i = 0
# 	print("N[%i] = %i" %(x,vet[x]))
