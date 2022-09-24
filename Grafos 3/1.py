from collections import defaultdict

class Grafo():
    def __init__(self):
        self.vertices = {}
        self.arestas = defaultdict(lambda: defaultdict(lambda: 0))
    
    def insere_v(self, id, dado):
        self.vertices[id] = dado
    
    def insere_a(self, id_o, id_d, peso):
        if ((id_o in self.vertices) and (id_d in self.vertices)):
            self.arestas[id_o][id_d] = peso

    def printMatriz(self):
        for v1 in sorted(self.vertices):
            for v2 in sorted(self.vertices):
                print(f"{self.arestas[v1][v2]}".rjust(4), end="")
            print()

    
            


grafo = Grafo()
num_v, num_a, n_dir = input().split()
for v in range(int(num_v)):
    grafo.insere_v(v+1, v+1)

n_dir = (n_dir == "N")

for _ in range(int(num_a)):
    v_o, v_d, peso = map(int, input().split())
    grafo.insere_a(v_o, v_d, peso)
    if n_dir:
        grafo.insere_a(v_d, v_o, peso)

grafo.printMatriz()