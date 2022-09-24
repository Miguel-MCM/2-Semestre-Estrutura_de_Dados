def nivel(raiz, dado, n=0):
    if raiz:
        if raiz.dado == dado:
            return n
        else:
            return max(nivel(raiz.esq,dado, n=n+1), nivel(raiz.dir, dado, n=n+1))
    else:
        return -1
    