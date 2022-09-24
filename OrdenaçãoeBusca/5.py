a, t = map(int, input().split())
alunos = []

for i in range(a):
    entrada = input()
    ira = float(entrada[0:4])
    nome = entrada[5:]
    alunos.append((ira, nome))

alunos.sort(reverse=True)

for i in range(t):
    alun = alunos[int(input())-1]
    print(f"{alun[1]} ({alun[0]:.2f})")