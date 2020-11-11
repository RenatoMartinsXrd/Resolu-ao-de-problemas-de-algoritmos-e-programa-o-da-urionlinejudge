idade_mae = int(input());
idade_filho1 = int(input());
idade_filho2 = int(input());
idade_filho3 = idade_mae - idade_filho1 - idade_filho2;
maior = idade_filho1 if idade_filho1>idade_filho2 else idade_filho2
print(idade_filho3 if idade_filho3>maior else maior )