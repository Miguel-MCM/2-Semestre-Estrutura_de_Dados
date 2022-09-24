n = int(input())

chamadas = [0]

def fibonacci(n):
    while n+1 > len(chamadas):
        chamadas.append(0)

    chamadas[n] += 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(f'fibonacci({n}) = {fibonacci(n)}.')
for i in range(len(chamadas)):
    print(f'{chamadas[i]} chamada(s) a fibonacci({i}).')

