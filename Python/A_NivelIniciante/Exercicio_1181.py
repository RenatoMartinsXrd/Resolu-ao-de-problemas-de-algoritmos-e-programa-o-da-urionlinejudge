def soma(linha,linha2):
 soma = 0
 for x in range(144):
  valor = float(input())
  if(x>=linha and x<linha2):
	  soma+=valor
 return soma
linha = int(input())
linha = linha * 12
linha2 = linha+12 if linha!=0 else 12
somaOuMedia = input()
resultado = soma(linha,linha2) 
print("%.1f" %(resultado if somaOuMedia =="S" else resultado/12))


