class Node():
    def __init__(self, dado, esq=None,dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir
    
    def add(self, dado):
        if dado < self.dado:
            if self.dir:
                self.dir.add(dado)
            else:
                self.dir = Node(dado)
        else:
            if self.esq:
                self.esq.add(dado)
            else:
                self.esq = Node(dado)
    
    def infixa(self):
        if self.dir:
            self.dir.infixa()
        print(self.dado,end=" ")
        if self.esq:
            self.esq.infixa()

    def posfixa(self):
        if self.dir:
            self.dir.posfixa()
        if self.esq:
            self.esq.posfixa()
        print(self.dado,end=" ")

    def prefixa(self):
        print(self.dado,end=" ")
        if self.dir:
            self.dir.prefixa()
        if self.esq:
            self.esq.prefixa()

    
    
raiz = None
while 1:
    entrada = input()
    if entrada == "quack":
        break
    elif entrada.isdigit():
        if not raiz:
            raiz = Node(int(entrada))
        else:
            raiz.add(int(entrada))
    elif entrada == 'in':
        if raiz:
            raiz.infixa()
        print()
    elif entrada == 'pos':
        if raiz:
            raiz.posfixa()
        print()
    elif entrada == 'pre':
        if raiz:
            raiz.prefixa()
        print()
    
    