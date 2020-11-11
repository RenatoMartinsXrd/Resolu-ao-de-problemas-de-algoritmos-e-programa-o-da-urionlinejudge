import re
leia = int(input())
lista = list()
codigo = ""
for x in range(leia):
    j = []
    codigo = ""
    frase = input()
    j = re.split(" +",frase)
    for z in range(len(j)):
        string = j[z]
        if string!="":
            codigo = codigo + string[0]
    print(codigo)
