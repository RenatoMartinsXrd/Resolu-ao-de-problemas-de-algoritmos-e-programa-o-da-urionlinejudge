i = 0
j1 = 1
j2 = 2
j3 = 3
print("I=%d J=%d" %(i,j1))
print("I=%d J=%d" %(i,j2))
print("I=%d J=%d" %(i,j3))
for x in range(4):
	i+=0.2
	j1+=0.2
	j2+=0.2
	j3+=0.2
	print("I=%.1f J=%.1f" %(i,j1))
	print("I=%.1f J=%.1f" %(i,j2))
	print("I=%.1f J=%.1f" %(i,j3))
i+=0.2
j1+=1
j2+=0.2
j3+=0.2
print("I=%d J=%d" %(i,j1))
print("I=%d J=%d" %(i,j2))
print("I=%d J=%d" %(i,j3))
j1-=0.8
for x in range(4):
	i+=0.2
	j1+=0.2
	j2+=0.2
	j3+=0.2
	print("I=%.1f J=%.1f" %(i,j1))
	print("I=%.1f J=%.1f" %(i,j2))
	print("I=%.1f J=%.1f" %(i,j3))
i+=1
j1+=0.2
j2+=0.2
j3+=0.2
print("I=%d J=%d" %(i,j1))
print("I=%d J=%d" %(i,j2))
print("I=%d J=%d" %(i,j3))