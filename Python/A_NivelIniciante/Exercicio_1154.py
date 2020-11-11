idade = 0
qtd = 0
soma = 0
while(True):
	idade = int(input())
	if idade<0:
		break
	soma+=idade
	qtd+=1
print("%.2f" %(soma/qtd))