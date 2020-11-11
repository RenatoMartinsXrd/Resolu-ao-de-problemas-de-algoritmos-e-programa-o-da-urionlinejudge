while True:
	try:
		string = input()
		count = 0
		troca = False
		if string[0]==")":
			print("incorrect")
			continue
		elif string[len(string)-1]=="(":
			print("incorrect")
			continue
		for c in string:
			if c=="(":
				count+=1
				troca = True
			elif c==")":
				count-=1
				troca = True
		print("correct" if count==0 and troca==True else "incorrect")
	except EOFError:
		break

