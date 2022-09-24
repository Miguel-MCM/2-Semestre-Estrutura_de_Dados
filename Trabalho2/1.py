class Node():
    def __init__(self , dado) -> None:
        self.dado = dado
        self.children = []

    def addChild(self, child):
        node_child = Node(child)
        self.children.append(node_child)
        return node_child

    def mostra(self, pref, n=0):
        print(pref*n, end='')
        print(self.dado)
        for f in self.children:
            f.mostra(pref, n=n+1)

    def numV(self):
        if self.dado == "V":
            return 1
        return sum([f.numV() for f in self.children])
    
    def numF(self):
        if self.children:
            return sum([f.numF() for f in self.children])
        return 1 

    def probtree(self):
        if self.dado == "V":
            return 100.0
        elif self.dado in "DE":
            return 0.0
        else:
            return (self.numV() / self.numF()) * 100

    def mostraProb(self, pref, n=0):
        print(pref*n, end='')
        print(f"{self.dado} ({self.probtree() :.2f}%)")
        for f in self.children:
            f.mostraProb(pref, n=n+1)


def montaArvore(raizes):
    # colocar os filhos da raiz
    filhos = []
    for r in raizes:
        for f in range(r[1]):
            filho, num_n = input().split()
            node_filho = r[0].addChild(filho)
            num_n = int(num_n)
            filhos.append((node_filho, num_n))

    if filhos:
        montaArvore(filhos)
    

comando = input()
if comando != "":
    comando = comando.split()
    if len(comando) == 2:
        raiz, num_f = comando
        num_f = int(num_f)
        raiz = Node(raiz)
        montaArvore([(raiz, num_f)])
comando = input()
if raiz:
    if comando == "gametree":
        raiz.mostra("__")
    elif comando == "probtree":
        raiz.mostraProb("..")