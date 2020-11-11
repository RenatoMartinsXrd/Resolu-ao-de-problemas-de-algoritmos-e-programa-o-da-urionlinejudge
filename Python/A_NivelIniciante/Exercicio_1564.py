while True:
  try:
      numero = int(input())
      if numero>0:
          print("vai ter duas!")
      else:
          print("vai ter copa!")
  except EOFError:
    break