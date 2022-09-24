o,d,t,i = map(int, input().split())
p = (2*o) + (3*d) + t

lista = [(p, i>=60, d, o, i,True)]

for _ in range(int(input())):
    o,d,t,i = map(int, input().split())
    p = (2*o) + (3*d) + t
    lista.append((p, i>=60, d, o, i,False))

lista.sort(reverse=True)
for i in range(len(lista)):
    if lista[i][5]:
        print(i+1)

