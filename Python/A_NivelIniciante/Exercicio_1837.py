# linha = input().split(" ")
# n1 = int(linha[0])
# n2 = int(linha[1])
# quociente = int(n1/n2)
# resto = int(n1-(n2*quociente))
# print("%.0f %.0f"%(quociente,resto))

data = input().split() 
a = int(data[0]) 
b = int(data[1]) 
div = divmod(a, abs(b)) 
if b < 0:
	print(-div[0], div[1]) 
else:
	print(div[0], div[1])