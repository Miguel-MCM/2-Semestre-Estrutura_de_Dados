def mostra(raiz, pref, n=0):
    if raiz:
        print(pref*n, end='')
        print(raiz.dado)
        for f in raiz.filhos:
            mostra(f, pref, n=n+1)