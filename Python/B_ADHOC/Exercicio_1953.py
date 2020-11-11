while True:
	try:
		chamada = {"EPR" : 0,"EHD":0}
		n = int(input())
		intrusos = 0
		for x in range(n):
			key = input().split()[1]
			if key in chamada:
				chamada[key]+=1
			else:
				intrusos+=1
		print("EPR: %d" %chamada["EPR"])
		print("EHD: %d" %chamada["EHD"])
		print("INTRUSOS: %d" %intrusos)
	except EOFError:
		break
