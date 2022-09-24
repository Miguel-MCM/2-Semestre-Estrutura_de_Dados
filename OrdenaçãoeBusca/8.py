# Prioridades
#   1. dec mod por k, negativo tem modulo negativo
#   2. par sobre impar
#   3.Depende
#       3.1 Empate Par: Maior
#       3.2 Empate Impar: Menor
def prioridades(num, fator):
    # 1
    p1 = abs(num) % fator
    if num < 0:
        p1 *= -1
    # 2
    p2 = not(num % 2)

    # 3
    if p2:
        p3 = num
    else:
        p3 = -num

    return [p1,p2,p3]


n, k = map(int, input().split())

nums = []
for _ in range(n):
    nums.append(int(input()))


nums.sort(key=lambda n: prioridades(n,k), reverse=True)

for i in range(len(nums)-1):
    print(nums[i],end=' ')
print(nums[-1])