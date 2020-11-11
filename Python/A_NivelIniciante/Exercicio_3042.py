while True:
    n = int(input())
    if n==0:
        break;
    atualIndex = 1
    qtdPolegada = 0
    caminho = {"0": 0,"1":-1}
    for x in range(n):
        linha = input()
        caminho["1"] = -1 
        caminho[linha[0]] = 0
        caminho[linha[2]] = 1
        caminho[linha[4]] = 2
        if caminho["1"]!=-1:
            qtdPolegada+=abs(atualIndex - caminho["0"])
            atualIndex = caminho["0"]
    print(qtdPolegada)
    
