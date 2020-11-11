acesso = False
while acesso==False:
    try:
        senha = int(input())
        acesso = True if senha==2002 else False
        prints = "Acesso Permitido" if acesso == True else "Senha Invalida"
        print(prints)
    except EOFError:
        break
