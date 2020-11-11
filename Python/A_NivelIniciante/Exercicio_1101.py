a,b = "",""

while True:
    menor,maior,soma = 0,0,0
    string = ""
    linha1 = input()
    a,b = linha1.split()
    a,b = int(a),int(b)
    if a<=0 or b<=0:
        break
    maior,menor = a if a>b else b,a if a<b else b
    for x in range(menor,maior+1):
        string = string + str(x) + " "
        soma = soma + x
    string = string + "Sum=" + str(soma)
    print(string)
