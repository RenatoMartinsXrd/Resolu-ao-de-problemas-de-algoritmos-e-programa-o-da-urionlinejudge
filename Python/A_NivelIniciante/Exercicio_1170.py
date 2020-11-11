n = int(input())
for x in range(n):
	dias = 0
	kg = float(input())
	while(kg>1):
		kg/=2
		dias = dias + 1
	print("%d dias" %dias)