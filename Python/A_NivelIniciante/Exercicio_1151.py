a = int(input())
penultimo = ultimo = 1
lista = list()
for x in range(a):
    if x>=3:
        agora = penultimo + ultimo
        lista.append(str(agora))
        penultimo = ultimo
        ultimo = agora
    elif x==0:
        lista.append(str(0))
    else:
        lista.append(str(ultimo))
print(" ".join(lista))
