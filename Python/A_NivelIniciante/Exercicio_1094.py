leia = int(input())
cobaias = 0
rato,sapo,coelho = 0,0,0
for x in range(leia):
    linha = input().split()
    qtd,qualCobaia = linha
    cobaias = cobaias + int(qtd)
    if qualCobaia=="C":
        coelho = coelho + int(qtd)
    elif qualCobaia=="R":
        rato = rato + int(qtd)
    elif qualCobaia=="S":
        sapo = sapo + int(qtd)
print("Total: %d cobaias" %cobaias)
print("Total de coelhos: %d" %coelho)
print("Total de ratos: %d" %rato)
print("Total de sapos: %d" %sapo)
print("Percentual de coelhos: %.2f %%" %((coelho/cobaias)*100))
print("Percentual de ratos: %.2f %%" %((rato/cobaias)*100))
print("Percentual de sapos: %.2f %%" %((sapo/cobaias)*100))
