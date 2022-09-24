# ArvoreBinaria
## dado
## esq
## dir

def altura(root, first=True):
    if root and not first:
        return(1 + max(altura(root.dir, first=False), altura(root.esq, first=False)))
    if root:
        return(max(altura(root.dir, first=False), altura(root.esq, first=False)))
    return 0