vetor = []
for x in range(20):
	vetor.append(int(input()))

c = 0
for i in range(19,-1,-1):
	x = vetor[c]
	vetor[c] = vetor[i]
	vetor[i] = x
	print("N[%d] = %d" %(c,vetor[i]))
	c+=1