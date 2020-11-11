n = int(input())
for x in range(n):
	altura,espessura,galhos = input().split(" ");
	print("Sim" if int(altura)>=200 and int(altura)<=300 and int(espessura)>=50 and int(galhos)>=150 else "Nao")
