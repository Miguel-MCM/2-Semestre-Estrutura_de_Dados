from collections import defaultdict

class Grafo():
    def __init__(self):
        self.vertices = []
        self.arestas = defaultdict(lambda: list())
    
    def insere_v(self, id):
        self.vertices.append(id)
    
    def insere_a(self, id_o, id_d):
        if ((id_o in self.vertices) and (id_d in self.vertices) and (id_d not in self.arestas[id_o])):
            self.arestas[id_o].append(id_d)

    def _alcancavel(self, id_o, id_d, vert):
        if id_d in self.arestas[id_o]:
            return True
        vert.remove(id_o)
        eh_alcancavel = False
        for i in self.arestas[id_o]:
            if i in vert:
                eh_alcancavel = self._alcancavel(i, id_d, vert)
                if eh_alcancavel:
                    return True
        return eh_alcancavel

    def alcancavel(self, id_o, id_d):
        vert = self.vertices.copy()
        return self._alcancavel(id_o, id_d, vert)

    def ciclico(self):
        for v in self.vertices:
            if self.alcancavel(v,v):
                return True
        return False

grafo = Grafo()

for _ in range(int(input())):
    id, lixo, *arestas = input().split()
    del lixo
    grafo.insere_v(id)
    for a in arestas:
        if a not in grafo.vertices:
            grafo.insere_v(a)
        grafo.insere_a(id, a)

if grafo.ciclico():
    print("Hoje tem!")
else:
    print("... que ama ninguem.")