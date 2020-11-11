
i = 1
maiorPalavra = 0
palavras = []
contadorPalavras = 0
palavraslocal = []
maiorPalavras = []
palavra = ""
while i!=0:
    i = int(input())
    contadorPalavras = contadorPalavras + i
    palavraslocal = []
    maiorPalavra = 0
    for x in range(i):
        palavra = input()
        palavraslocal.append(palavra)
        if len(palavra)>maiorPalavra:
            maiorPalavra = len(palavra)
    palavras.append(palavraslocal)
    maiorPalavras.append(maiorPalavra)
for y in range(len(palavras)):
    palavrasz = palavras[y]
    numeroMaiorPalavra = maiorPalavras[y]
    if y>0 and y<len(palavras)-1:
        print("")
    for z in range(len(palavrasz)):
        if len(palavrasz[z])<numeroMaiorPalavra:
            espaços = numeroMaiorPalavra - len(palavrasz[z])
            string = palavrasz[z]
            es = " "
            espaços -=1
            for t in range(espaços):
               es = es + " "
            string = es + string[::]
            print(string)
        else:
            print(palavrasz[z])
    
