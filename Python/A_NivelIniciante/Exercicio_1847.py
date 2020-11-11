linha= input().split(" ")
A = int(linha[0])
B = int(linha[1])
C = int(linha[2])

if(B<A): #temperatura caiu
	if(C>=B):
		print(":)")
	else:
		dia1 = A - B
		dia2 = B - C
		if(dia2<dia1):
			print(":)")
		else:
			print(":(")
elif(B>A):
	if(C<=B):
		print(":(")
	else:
		dia1 = B - A
		dia2 = C - B
		if(dia2<dia1):
			print(":(")
		else:
			print(":)")
elif(A==B and C>B):
	print(":)")
else:
	print(":(")



#temperatura Subiu
