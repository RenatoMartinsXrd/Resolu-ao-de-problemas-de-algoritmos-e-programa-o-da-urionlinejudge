criancas = int(input())
f = m = 0
for x in range(criancas):
    string = input()
    if string.endswith("M"):
        m+=1
    else:
        f+=1
print("%d carrinhos" %m)
print("%d bonecas" %f)
