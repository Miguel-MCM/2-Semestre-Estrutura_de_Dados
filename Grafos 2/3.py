from collections import defaultdict

class Grafo():
    def __init__(self):
        self.vertices = {}
        self.arestas = defaultdict(lambda: list())
    
    def insere_v(self, id, dado):
        self.vertices[id] = dado
    
    def insere_a(self, id_o, id_d, peso):
        if ((id_o in self.vertices) and (id_d in self.vertices)):
            self.arestas[id_o].append((id_d, peso))

    def Distancia(self, id_o, id_d):
        if id_o == id_d:
            return 0
        vizitados = [id_o]
        opc = [(vizinho[0] , vizinho[1]) for vizinho in self.arestas[id_o]]
        while opc != []:
            escolhido = opc.pop()
            if escolhido[0] == id_d:
                return escolhido[1]
            vizitados.append(escolhido[0])
            for vizinho in self.arestas[escolhido[0]]:
                if vizinho[0] not in vizitados:
                    opc.insert(0, (vizinho[0], escolhido[1]+vizinho[1]))
        return None

    def grau_saida(self, id):
        if id in self.arestas:
            return len(self.arestas[id])
        return 0

    def maiorLigacao(self):
        sub_grafo = Grafo()
        for i in range(len(self.vertices) - 1):
            id = list(self.vertices.keys())[i]
            sub_grafo.insere_v(id, id)
            opc = self.arestas[id].copy()
            for o in opc.copy():
                if (o[0] in sub_grafo.arestas) and (id in [a[0] for a in sub_grafo.arestas[o[0]]]):
                    opc.remove(o)
            aresta = max(opc, key=lambda o: o[1])
            if aresta[0] not in sub_grafo.vertices:
                sub_grafo.insere_v(aresta[0], aresta[0])
            sub_grafo.insere_a(id, aresta[0], aresta[1])

        d = 0
        for v in sub_grafo.arestas:
            for a in sub_grafo.arestas[v]:
                d += a[1]
        return d
        


    # def maiorCaminho(self):
    #     # Achar a maior aresta
    #     caminho = []

    #     id_i = None
    #     maior_a = [None, 0]
    #     for id in self.arestas:
    #         for a in self.arestas[id]:
    #             if a[1] > maior_a[1]:
    #                 id_i = id
    #                 maior_a = a
    #     caminho.append(id_i)
    #     caminho.append(maior_a[0])
    #     d = maior_a[1]

    #     # Ir seguindo pela maior aresta para vertices que eu ainda não passei
    #     opc = self.arestas[maior_a[0]].copy()
    #     while opc:
    #         to_remove = []
    #         for o in opc:
    #             if o[0] in caminho:
    #                 to_remove.append(o)
    #         for o in to_remove:
    #             opc.remove(o)
    #         if not opc:
    #             break
    #         maior_a = max(opc, key=lambda o: o[1])
    #         caminho.append(maior_a[0])
    #         d += maior_a[1]
    #         opc = self.arestas[maior_a[0]].copy()
    #     return caminho
            
    # def calculaDistancia(self, caminho):
    #     d = 0
    #     for i in range(len(caminho) - 1):
    #         for a in self.arestas[caminho[i]]:
    #             if a[0] == caminho[i+1]:
    #                 d += a[1]
    #                 break
    #     return d


grafo = Grafo()

for i in range(int(input())):
    id, numA, *arestas = input().split()
    del numA
    grafo.insere_v(id, id)
    while arestas != []:
        id_v = arestas.pop()
        peso = arestas.pop()
        if id_v not in grafo.vertices:
            grafo.insere_v(id_v,id_v)

        grafo.insere_a(id, id_v, int(peso))


print(f"R${grafo.maiorLigacao() * 3.14 : 0.2f}")
    
