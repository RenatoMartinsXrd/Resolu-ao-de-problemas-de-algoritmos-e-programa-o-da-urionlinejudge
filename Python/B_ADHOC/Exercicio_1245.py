import re
while True:
  try:
      pares = 0
      myMap = {}
      n = int(input())
      a = ""
      for z in range(n):
        line = input().split(" ");
        numeroBota = int(line[0])
        
        if numeroBota in myMap:
          a = myMap.get(numeroBota)+line[1]
          myMap[numeroBota] = a
        else:
          myMap[numeroBota] = line[1]


      for x in myMap:
        D = len(re.findall("D", myMap[x]))
        E = len(re.findall("E", myMap[x]))
        if D>E and E!=0:
            pares+=E
        elif E>D and D!=0:
            pares+=D
        elif E==D:
            pares+=E
      print(pares)
  except EOFError:
    break
