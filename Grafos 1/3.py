from collections import defaultdict

class Grafo():
    def __init__(self):
        self.vertices = {}
        self.arestas = defaultdict(lambda: list())
    
    def insere_v(self, id, dado):
        self.vertices[id] = dado
    
    def insere_a(self, id_o, id_d):
        if (id_o in self.vertices) and (id_d in self.vertices):
            self.arestas[id_o].append(id_d)
        
    def remove_v(self, id):
        if id in self.vertices:
            self.vertices.pop(id)
            for i in self.arestas:
                if i == id:
                    self.arestas.pop(i)
                else:
                    if id in self.arestas[i]:
                        self.arestas[i].remove(id)
    
    def remove_a(self, id_o, id_d):
        if id_o in self.arestas:
            if id_d in self.arestas[id_o]:
                self.arestas[id_o].remove[id_d]
    
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

grafo = Grafo()
n = int
for i in range(n):
    comando, id, *argm = input()
    if comando == "IV":
        grafo.insere_v(id, argm[0])
    elif comando == "IA":
        grafo.insere_a(id, argm[0])
    elif comando == "RV":
        grafo.remove_v(id)
    elif comando == "RA":
        grafo.remove_a(id, argm[0])
                


