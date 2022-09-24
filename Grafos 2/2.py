from collections import defaultdict

class Grafo():
    def __init__(self):
        self.vertices = {}
        self.arestas = defaultdict(lambda: list())
    
    def insere_v(self, id, dado):
        self.vertices[id] = dado
    
    def insere_a(self, id_o, id_d):
        if ((id_o in self.vertices) and (id_d in self.vertices) and (id_d not in self.arestas[id_o])):
            self.arestas[id_o].append(id_d)
        
    def remove_v(self, id):
        if id in self.vertices:
            self.vertices.pop(id)
            if id in self.arestas:
                self.arestas.pop(id)
            for i in self.arestas:
                if id in self.arestas[i]:
                    self.arestas[i].remove(id)
    
    def remove_a(self, id_o, id_d):
        if id_o in self.arestas:
            if id_d in self.arestas[id_o]:
                self.arestas[id_o].remove(id_d)
    
    def grau_saida(self, id):
        if id in self.arestas:
            return len(self.arestas[id])
        return 0
    
    def grau_entrada(self, id):
        grau = 0
        for i in self.arestas:
            if id in self.arestas[i]:
                grau += 1
        return grau

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

    def minGrau(self):
        if self.vertices:
            graus = [self.grau_saida(i) for i in self.vertices]
            return min(graus)
        return 0

    def Distancia(self, id_o, id_d):
        if id_o == id_d:
            return 0
        vizitados = [id_o]
        opc = [(vizinho , 0) for vizinho in self.arestas[id_o]]
        while opc != []:
            escolhido = opc.pop()
            if escolhido[0] == id_d:
                return escolhido[1]
            vizitados.append(escolhido[0])
            for vizinho in self.arestas[escolhido[0]]:
                if vizinho not in vizitados:
                    opc.insert(0, (vizinho, escolhido[1]+1))
        return None

grafo = Grafo()

for _ in range(int(input())):
    id, lixo, *arestas = input().split()
    del lixo
    grafo.insere_v(id, id)
    for a in arestas:
        if a not in grafo.vertices:
            grafo.insere_v(a,a)
    grafo.insere_a(id, a)

eu, mussum = input().split()
d = grafo.Distancia(eu, mussum)
if d is not None:
    print(d)
else:
    print("Forevis alonis...")

