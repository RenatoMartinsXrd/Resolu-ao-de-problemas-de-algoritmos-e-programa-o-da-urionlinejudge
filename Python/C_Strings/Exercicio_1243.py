import re
while True:
    try:
        soma = 0
        media = 0
        qtd = 0
        string = input()
        palavras = string.split(" ");
        for x in palavras:
            if not x:
                continue
            if re.search("[0-9]+", x):
                continue
            elif x.startswith("."):
                continue
            if x.endswith("."):
                x = x[:len(x)-1]
                a = re.match("^(?!.*[\.0-9]).*$",x)
                if a:
                    soma+=len(a.group())
                    qtd+=1
                continue;
            if re.search("\.+",x):
                continue
            else:
                soma+=len(x)
                qtd+=1
        if qtd!=0:
            media = soma//qtd
        if media<=3:
            print(250)
        elif media==4 or media==5:
            print(500)
        elif media>=6:
            print(1000)     
    except EOFError:
        break   