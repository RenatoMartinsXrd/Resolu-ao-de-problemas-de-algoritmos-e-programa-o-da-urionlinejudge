soma = 0
operacao = input()
h = 11
for x in range(12):
    for z in range(12):
        number = float(input())
        if z>x and z<h and x<=4:
            soma+=number
    h-=1
if operacao =="S":
    print("%.1f" %soma)
elif operacao=="M":
    print("%.1f" %(soma/30))

