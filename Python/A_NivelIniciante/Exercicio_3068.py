contador = 1
while(True):
	qtd = 0
	coordenadas = input().split(" ")
	x1 = int(coordenadas[0])
	y1 = int(coordenadas[1])
	x2 = int(coordenadas[2])
	y2 = int(coordenadas[3])
	if(x1==x2==y2==y1==0):
		break

	if x1>x2:
		x2,x1 = x1,x2
	if y1>y2:
		y2,y1 = y1,y2 
	
	quantidadeMeteoros = int(input())
	for z in range(quantidadeMeteoros):
		coordenadasMeteoros = input().split(" ")
		x = int(coordenadasMeteoros[0])
		y = int(coordenadasMeteoros[1])
		if x>=x1 and x<=x2 and y>=y1 and y<=y2:
			qtd = qtd + 1
	print("Teste")
	print(contador)
	print(qtd)
	contador = contador + 1

