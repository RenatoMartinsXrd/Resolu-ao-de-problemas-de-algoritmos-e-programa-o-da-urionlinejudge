codigo = 1
contador = 0
nota = list()
while codigo==1:
    if contador<2:
        verifica = float(input())
        if verifica<0 or verifica>10:
            print("nota invalida")
        else:
            nota.append(verifica)
            contador+=1
    else:
        contador = 0
        print("media = %.2f" %((nota[0]+nota[1])/2))
        nota = list()
        codigo = 0
        while codigo!=1 and codigo!=2:
            print("novo calculo (1-sim 2-nao)")
            codigo = int(input())
