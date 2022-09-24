discos, torreA, torreB, torreC = input().split()
discos = int(discos)

def moveTorre(n, inic, aux, fim):
    if n == 1:
        print(f"Mover de {inic} para {fim}.")
    else:
        moveTorre(n-1, inic, fim, aux)
        print(f"Mover de {inic} para {fim}.")
        moveTorre(n-1, aux, inic, fim)

moveTorre(discos, torreA, torreC, torreB)
    