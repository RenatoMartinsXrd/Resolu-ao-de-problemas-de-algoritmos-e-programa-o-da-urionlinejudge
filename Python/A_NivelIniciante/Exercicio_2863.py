contador = 0
menor = 0
anterior = 0
numeroTeste = int(input())
while True:
    try:
        if contador<numeroTeste:
            contador = contador + 1
            atual = float(input())
            menor = atual if atual<anterior else menor
            anterior = atual
        else:
            contador = 0
            print(menor)
            numeroTeste = int(input())
    except EOFError:
        break
