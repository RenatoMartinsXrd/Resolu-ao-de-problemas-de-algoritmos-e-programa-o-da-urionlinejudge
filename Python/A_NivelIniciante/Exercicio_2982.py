entrada = int(input())
eae = {"G":0,"V":0}
for x in range(entrada):
	fodase = input().split(" ")
	eae[fodase[0]] = eae[fodase[0]]+int(fodase[1])
print("NAO VAI TER CORTE, VAI TER LUTA!" if eae["G"]>eae["V"] else "A greve vai parar.")