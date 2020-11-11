leia = int(input())
linha = input()
teste = linha.split()
menor = int(teste[0])
posicao = 0
for x in range(leia):
    teste[x] = int(teste[x])
    if teste[x]<menor:
        menor = teste[x]
        posicao = x
print("Menor valor: %d\nPosicao: %d" %(menor,posicao))    
