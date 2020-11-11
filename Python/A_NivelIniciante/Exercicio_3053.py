n = int(input())
atual = {"A":0,"B":0,"C":0}
letra = input()
atual[letra] = 1
local = letra 
for x in range(n):
	movimento = int(input())
	if atual["A"]==1:
		if movimento==1:
			atual["B"]=1
			atual["A"]=0
			local = "B"
		elif movimento==2:
			continue
		elif movimento==3:
			atual["C"]=1
			atual["A"]=0
			local = "C"	
	elif atual["B"]==1:
		if movimento==1:
			atual["A"]=1
			atual["B"]=0
			local = "A"
		elif movimento==2:
			atual["C"]=1
			atual["B"]=0
			local = "C"
		elif movimento==3:
			continue
	elif atual["C"]==1:
		if movimento==1:
			continue
		elif movimento==2:
			atual["C"]=0
			atual["B"]=1
			local = "B"
		elif movimento==3:
			atual["C"]=0
			atual["A"]=1
			local = "A"
print(local)