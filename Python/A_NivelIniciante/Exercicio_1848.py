caw = 0
soma = 0
def covertaByDecimal(num):
	resultado = 0
	cont =len(num)
	for i in range(cont):
		cont = cont - 1
		if num[cont]=="0":
			continue
		else:
			resultado+=2**i
	return resultado

while caw<3:
	entrada = input()
	binario = ""
	if entrada!="caw caw":
		binario+="0" if entrada[0]=="-" else "1"
		binario+="0" if entrada[1]=="-" else "1"
		binario+="0" if entrada[2]=="-" else "1"
		soma+=covertaByDecimal(binario)
	else:
		print(soma)
		soma = 0
		caw+=1
