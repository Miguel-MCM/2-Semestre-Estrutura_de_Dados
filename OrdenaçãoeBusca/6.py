dicMencoes = {"SS":0,"MS":1,"MM":2,"MI":3,"II":4,"SR":5}

alunos = []
for _ in range(int(input())):
    entrada = input()
    men = entrada[:2]
    nome = entrada[3:]
    alunos.append((men,nome))

alunos.sort(key=lambda a: (dicMencoes[a[0]],a[1]))
for a in alunos:
    print(f"{a[0]} {a[1]}")