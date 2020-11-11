n = int(input())
for x in range(n):
	a = ""
	operacao = input().split(" ")
	n1 = int(operacao[0])
	sinal = operacao[1]
	n2 = int(operacao[2])
	resultado = int(operacao[4])
	if sinal=="+":
		print("E"+a.rjust((abs((n1+n2) - resultado)),"r")+"ou!")
	elif sinal=="x":
		print("E"+a.rjust((abs((n1*n2) - resultado)),"r")+"ou!")
	elif sinal=="-":
		print("E"+a.rjust((abs((n1-n2) - resultado)),"r")+"ou!")