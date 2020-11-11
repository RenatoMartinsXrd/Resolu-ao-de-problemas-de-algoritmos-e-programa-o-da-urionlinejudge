import re
while True:
  try:
      palavra = input()
      palavra = re.sub("o","0",palavra)
      palavra = re.sub("O","0",palavra)
      palavra = re.sub("l","1",palavra)
      palavra = re.sub(" ","",palavra)
      palavra = re.sub(",","",palavra)
      #palavra = re.sub('[^0-9]', '', palavra)
      numero = 0
      try:
        numero = int(palavra)
        if palavra=="" or palavra==" ":
          print("error")
        elif int(palavra)>2147483647 and int(palavra)>0:
          print("error")
        else:
          print(int(palavra))
      except ValueError:
        print("error")

  except EOFError:
    break
