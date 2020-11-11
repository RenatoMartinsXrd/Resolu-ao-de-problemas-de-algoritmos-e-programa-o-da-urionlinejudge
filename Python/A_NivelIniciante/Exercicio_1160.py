leia = int(input())
for x in range(leia):
    anos = 0
    taxa1 = 0
    taxa2 = 0
    linha = input()
    populacaoA,populacaoB,crescimentoA,crescimentoB = linha.split()
    populacaoA = int(populacaoA)
    populacaoB = int(populacaoB)
    crescimentoA = float(crescimentoA)
    crescimentoB = float(crescimentoB)
    taxa1 = crescimentoA/100
    taxa2 = crescimentoB/100
    while populacaoA<=populacaoB and anos<=100:
        populacaoA = populacaoA + int(populacaoA * taxa1)
        populacaoB = populacaoB + int(populacaoB * taxa2)
        anos = anos + 1
    if anos>100:
        print("Mais de 1 seculo.")
    else:
        print("%d anos." %anos)
    
