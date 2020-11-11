leia = int(input())
leds = {"0":6,"1":2,"2":5,"3":5,"4":4,"5":5,"6":6,"7":3,"8":7,"9":6}
for z in range(leia):
	numeroleds = 0
	valor = input()
	for x in valor:
		numeroleds = numeroleds + leds[x]
	print("%d leds" %numeroleds)

