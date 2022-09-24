from collections import defaultdict



inf = defaultdict(lambda: defaultdict(lambda: 0))

for _ in range(int(input())):
    id, art = map(int, input().split())
    inf[id][art] += 1

for i in input().split():
    if i.isdigit():
        n = int(i)
        break

input()
for i in range(n):
    id = int(input())
    if not (id in inf.keys()):
        print(f"Grato, cidadao {id}.")
    else:
        print(f"Teje preso, {id}!")
        crimes = list(inf[id].items())
        crimes.sort(reverse=True,key=lambda i: (i[1],-i[0]))
        for c in crimes:
            print(f"- Art. {c[0]}: {c[1]} ocorrencia(s).")