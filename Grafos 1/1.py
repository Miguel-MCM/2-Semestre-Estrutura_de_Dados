
def EhSubgrafo(g1, g2):
    if g2:
        if g1:
            for id in g2:
                if id not in g1:
                    return False
                for v in g2[id]:
                    if v not in g1[id]:
                        return False
            return True
        return False
    return True
    

n = int(input())
grafo1 = {}
for i in range(n):
    id, numV, *verts = input().split()
    grafo1[id] = verts
input()
n2 = int(input())
grafo2 = {}
for i in range(n2):
    id, numV, *verts = input().split()
    grafo2[id] = verts

if EhSubgrafo(grafo1, grafo2):
    print("Sub-sub!")
else:
    print("Ue? Ue? Ue?")
