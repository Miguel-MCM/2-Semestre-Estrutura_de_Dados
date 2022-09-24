n = 1
while n:
    n = int(input())
    constantes = []
    if n == 0:
        break

    for _ in range(n):
        nome, lixo, real = input().split()
        del lixo

        real = float(real)
        inteiro = int(real)
        decimal = round(real - inteiro, 2)
        constantes.append((nome, real, inteiro, decimal))
    
    constantes.sort(key=lambda i: [i[3], -i[2]])

    nomes = [i[0] for i in constantes]
    print(" < ".join(nomes))

    
