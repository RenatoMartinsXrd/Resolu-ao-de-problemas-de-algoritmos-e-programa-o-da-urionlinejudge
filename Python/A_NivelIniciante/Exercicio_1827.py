def pontoCentral(matriz,tamanho):
    ponto = (tamanho-1)//2
    matriz[ponto][ponto] = 4

def preencher(tamanho,interna):
    matriz = []
    a = interna
    b = tamanho - interna
    for x in range(tamanho):
        matriz.append([0]*tamanho)
        if x>=interna and x<b:
            for z in range(interna,b):
                matriz[a][z] = 1
            a = a + 1
    return matriz

def externa(matriz):
    matriz[0][0] = 2
    matriz[0][tamanho-1] = 3
    matriz[tamanho-1][0] = 3
    matriz[tamanho-1][tamanho-1] = 2
    
def diagonais(matriz,tamanho):
    a = tamanho
    for x in range(tamanho//3):
        matriz[x][x] = 2
        matriz[x][a-1] = 3
        matriz[a-1][a-1] = 2
        matriz[a-1][x] = 3
        a = a-1
while True:
  try:
      tamanho = int(input())
      matriz = preencher(tamanho,tamanho//3)
      externa(matriz)
      diagonais(matriz,tamanho)
      pontoCentral(matriz,tamanho)
      for z in matriz:
          for x in z:
              print(x, end="")
          print("")
      print("")
  except EOFError:
    break
