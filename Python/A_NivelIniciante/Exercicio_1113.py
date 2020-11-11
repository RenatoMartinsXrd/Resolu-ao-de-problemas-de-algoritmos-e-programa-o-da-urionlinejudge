while(True):
	entrada = input().split(" ")
	first  = int(entrada[0])
	second = int(entrada[1])
	if(first>second):
		print("Decrescente")
	elif(second>first):
		print("Crescente")
	else:
		break
