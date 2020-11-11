a = int(input())
fora = dentro = 0
for x in range(a):
    b = int(input())
    if b>=10 and b<=20:
        dentro = dentro + 1
    else:
        fora = fora + 1
print("%d in" %dentro)
print("%d out" %fora)
        
