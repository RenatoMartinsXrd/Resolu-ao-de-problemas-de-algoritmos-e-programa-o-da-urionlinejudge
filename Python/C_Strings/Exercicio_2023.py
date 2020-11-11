from operator import itemgetter
dicionario = {}
while True:
    try:
        a= input()
        dicionario[a.lower()] = a
    except EOFError:
        break
c  = sorted(dicionario.items(), key=itemgetter(0))
print(c.pop()[1])
