porcao = [300,1500,600,1000,150]
soma = 0
for x in range(5):
    vezes = int(input())
    soma = (porcao[x] * vezes) + soma
print(soma + 225)
