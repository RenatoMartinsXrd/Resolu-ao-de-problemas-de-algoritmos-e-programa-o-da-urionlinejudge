n = int(input())
lancamento = []
for x in range(n):
	total1 = 0
	total2 = 0
	for z in range(3):
		lancamento = input().split(" ")
		total1+= int(lancamento[0]) * int(lancamento[1])
	for z in range(3):
		lancamento = input().split(" ")
		total2+= int(lancamento[0]) * int(lancamento[1])
	print("JOAO" if total1>total2 else "MARIA")