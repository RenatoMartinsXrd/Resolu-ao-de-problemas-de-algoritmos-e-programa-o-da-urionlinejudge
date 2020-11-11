import re
while True:
  try:
    contador = 1
    frase = input()
    letra = ""
    lista = []
    palavras = frase.split()
    listaletra = []
    for x in range(len(palavras)):
        s = palavras[x].lower()
        if s[0] != letra:
            letra = s[0]
        else:
            if x==1:
                lista.append(letra)
            elif x>1:
                if not lista:
                    lista.append(letra)
                elif letra!=lista[-1]:
                    lista.append(letra)
                elif letra == lista[-1]:
                    if letra!=listaletra[-2]:
                        lista.append(letra)            
        listaletra.append(letra)      
    print(len(lista))
  except EOFError:
    break
