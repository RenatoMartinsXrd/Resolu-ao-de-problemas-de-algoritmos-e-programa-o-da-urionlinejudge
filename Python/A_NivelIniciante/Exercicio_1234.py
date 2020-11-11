while True:
    try:
        s = input()
        string = ""
        contador = 0
        for letra in s:
            if letra==" ":
                string = string + letra
            elif contador%2==0:
                string = string + letra.upper()
                contador = contador + 1
            else:
                if letra == letra.upper():
                    letra = letra.lower()
                    string = string + letra
                    contador = contador + 1
                else:
                    string = string + letra
                    contador = contador + 1 
        print(string)
    except EOFError:
        break
