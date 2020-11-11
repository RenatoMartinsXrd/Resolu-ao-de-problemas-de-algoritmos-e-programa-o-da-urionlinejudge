pessoas = int(input())
soma = 0
for x in range(leia):
    dados.append(input())
    if x==1:
        beleza1,fortuna1,valor1 = dados[0].split()
        beleza2,fortuna2,valor2 = dados[1].split()
        if beleza1>=beleza2 and fortuna1<fortuna2:
        elif beleza2>=beleza1 and fortuna2<fortuan1:
        elif fortuna2>=fortuan1 and beleza1>=beleza2


ultimo = len(dados)
for z in range(leia):
    beleza1,fortuna1,valor1 = dados[z].split()
    beleza2,fortuna2,valor2 = dados[ultimo].split()
    if beleza1>beleza2 and fortuna1>fortuna2:
        dados[z],dados[ultimo] = dados[ultimo],dados[z]

