class Node():
    def __init__(self,dado):
        self.dado = dado
        self.esq = None
        self.dir = None
    
    def addDir(self,node):
        self.dir = node

    def addEsq(self,node):
        self.esq = node

def criaArv(arv):
    no = Node(0)

    num_prt = 1
    filho_esq = True

    i = 1
    while num_prt:
        if i == 1 and arv[i] == ")":
            return
        elif arv[i] == ")":
            num_prt -= 1
        elif arv[i] == "(":
            num_prt += 1
            if filho_esq:
                no.dado += 1
            else:
                no.dado -= 1
            if num_prt == 2:
                if filho_esq:
                    no.addEsq(criaArv(arv[i:]))
                    filho_esq = False
                else:
                    no.addDir(criaArv(arv[i:]))
                    filho_esq = True
        i += 1
    return no


def altura(root):
    if root:
        return(1 + max(altura(root.dir), altura(root.esq,)))
    return 0

def mostra(raiz):
    print("(", end='')
    if raiz:
        print(altura(raiz.esq) - altura(raiz.dir), end=' ')
        mostra(raiz.esq)
        print(' ',end='')
        mostra(raiz.dir)
    print(")", end='')

arvore = input()
raiz = criaArv(arvore)
mostra(raiz)