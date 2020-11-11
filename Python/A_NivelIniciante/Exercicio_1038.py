linha1 = input()
cod,qtd = linha1.split(" ")
cod = int(cod)
qtd = int(qtd)
total = 0
if cod==1:
    total = qtd * 4.00
elif cod==2:
    total = qtd * 4.50
elif cod==3:
    total = qtd * 5.00
elif cod==4:
    total = qtd * 2.00
elif cod==5:
    total = qtd * 1.50  
print("Total: R$ %.2f" %total)
