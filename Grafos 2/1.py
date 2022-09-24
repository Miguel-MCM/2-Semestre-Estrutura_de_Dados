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

grafo = Grafo()

for i in range(int(input())):
    comando, *argm = input().split()
    if comando == "IV":
        grafo.insere_v(argm[0], argm[0])
    elif comando == "IA":
        grafo.insere_a(argm[0], argm[1])
        grafo.insere_a(argm[1], argm[0])
    elif comando == "RV":
        grafo.remove_v(argm[0])
    elif comando == "RA":
        grafo.remove_a(argm[0], argm[1])
        grafo.remove_a(argm[1], argm[0])

print(grafo.minGrau())