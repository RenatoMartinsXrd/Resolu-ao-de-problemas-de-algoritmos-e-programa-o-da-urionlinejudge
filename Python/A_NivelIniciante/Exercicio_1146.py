while True:
    a = int(input())
    if a==0:
        break
    s = ""
    for y in range(1,a+1):
        s = s + str(y) + " "
    print(s.strip())
