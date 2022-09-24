pilotos = []

for i in range(int(input())):
    nome = input()
    t1, t2, t3 = map(float ,input().split())
    tot_sec = t1 + t2 + t3

    sec = tot_sec
    min = 0
    while (sec >= 60):
        min += 1
        sec -= 60


    pilotos.append((nome, tot_sec, min, sec))

pilotos.sort(key=lambda p: p[1])

for i in range(len(pilotos)):
    print(f"{i}. {pilotos[i][0]} ({pilotos[i][2]}:{pilotos[i][3]:06.3f})")

