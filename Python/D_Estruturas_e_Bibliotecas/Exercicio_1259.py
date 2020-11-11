a = int(input())
pares = list()
impares = list()
for x in range(a):
    b = int(input())
    if b%2==0:
        pares.append(b)
    else:
        impares.append(b)
pares.sort()
impares.sort(reverse=True)
for z in range(len(pares)):
    print(pares[z])
for i in range(len(impares)):
    print(impares[i])
