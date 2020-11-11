leia = int(input())
for x in range(leia):
    numeroEstudantes = int(input())
    estudantes = input()
    frequencia = input()
    estudantes = estudantes.split()
    frequencia = frequencia.split()
    faltosos = ""
    for z in range(numeroEstudantes):
        falta = 0
        presença = 0
        porcentagem = 0
        aluno = estudantes[z]
        numeroFreq = frequencia[z]
        total = len(numeroFreq)
        for p in range(len(numeroFreq)):
            
            if frequencia[z][p] =="P":
                presença = presença + 1
            elif frequencia[z][p]== "M":
                total = total - 1
        porcentagem = (presença/total)*100
        total = 0
        if porcentagem<75:
            faltosos = faltosos + " " +aluno
    print(faltosos.strip())
