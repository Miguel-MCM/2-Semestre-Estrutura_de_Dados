
n = int(input())
grafo = {}
for i in range(n):
    id, lixo, *arestas = input().split()
    del lixo
    grafo[id] = arestas


nao_amg = ["Mussum"]
for id in grafo:
    if id != "Mussum" and id not in grafo["Mussum"]:
        nao_amg.append(id)

sugestoes = []
for pessoa in nao_amg:
    if pessoa != "Mussum":
        cont = 0
        for id in grafo:
            if (id not in nao_amg) and (pessoa in grafo[id]):
                cont += 1
            if cont == 3:
                sugestoes.append(pessoa)
                break

if sugestoes:
    for s in sorted(sugestoes):
        print(s)
else:
    print("Cacildis! Cade elis?")