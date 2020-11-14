entrada = int(input())
for x in range(entrada):
    ano = int(input())
    if ano<2015:
        print("%d D.C." %(2015 - ano))
    else:
        print("%d A.C." %((ano - 2015)+1))

