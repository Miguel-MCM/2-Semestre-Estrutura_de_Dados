def constituiArvoreBinariaDeBusca(raiz):
    if raiz:
        if (raiz.esq and raiz.esq.dado > raiz.dado) or (raiz.dir and raiz.dir.dado < raiz.dado):
            return False
        return constituiArvoreBinariaDeBusca(raiz.esq) and constituiArvoreBinariaDeBusca(raiz.dir)
    return True