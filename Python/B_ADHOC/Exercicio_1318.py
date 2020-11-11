while True:
    a = input()
    if a[0]=="0":
        break
    b = input()
    qtd = 0
    convites = b.split(" ")
    clones = set()
    clones2 = set()
    for x in convites:
        if x in clones:
            if not x in clones2:
                clones2.add(x)
                qtd+=1
        else:
            clones.add(x)
    print(qtd)

