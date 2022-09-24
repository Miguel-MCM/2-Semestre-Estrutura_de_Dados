class Node():
    def __init__(self,dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir
    
    def addNode(self, addDado):
        if addDado < self.dado:
            if not self.esq:
                self.esq = Node(addDado)
            else:
                self.esq.addNode(addDado)
        else:
            if not self.dir:
                self.dir = Node(addDado)
            else:
                self.dir.addNode(addDado)
    

def prefixo(raiz):
    if raiz:
        return " " + str(raiz.dado) + prefixo(raiz.esq) +  prefixo(raiz.dir)
    return ''

def infixo(raiz):
    if raiz:
        return infixo(raiz.esq) + str(raiz.dado) + " " + infixo(raiz.dir)
    return ''

def posfixo(raiz):
    if raiz:
        return posfixo(raiz.esq) + posfixo(raiz.dir) + " " + str(raiz.dado)
    return ''


c = int(input())

for i in range(c):
    n = int(input())

    numeros = [int(x) for x in input().split()]
    if numeros:
        raiz = Node(numeros[0])
        for num in numeros[1:]:
            raiz.addNode(num)

        print(f"Case {i+1}:")
        print("Pre.: " + prefixo(raiz).strip())
        print("In..: " + infixo(raiz).strip())
        print("Post: " + posfixo(raiz).strip())
        print()
    

