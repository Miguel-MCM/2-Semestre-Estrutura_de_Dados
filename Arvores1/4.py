def rotaciona_direita(raiz):
    pass

def comprime(raiz, r):
    if raiz and r:
        n_raiz = rotaciona_direita(raiz)
        comprime(n_raiz.esq, r-1)
        return n_raiz
    return raiz
