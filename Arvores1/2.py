# ArvoreBinaria
## dado
## esq
## dir

def mostra(raiz):
    print("(", end='')
    if raiz:
        print(raiz.dado, end=' ')
        mostra(raiz.esq)
        print(' ',end='')
        mostra(raiz.dir)
    print(")", end=' ')

        