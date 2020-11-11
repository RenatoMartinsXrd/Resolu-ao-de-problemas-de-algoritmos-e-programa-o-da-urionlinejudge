j = 7
i = 1
contador = 0
for x in range(15):
    if contador==3:
        contador = 0
        j = 7
        i = i + 2
    print("I=%d J=%d" %(i,j))
    contador = contador + 1
    j = j - 1
