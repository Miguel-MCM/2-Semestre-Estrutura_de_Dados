n = int(input())

def soma(nums):
    if len(nums) == 1:
        print(nums[0])
    else:
        print(f"{nums[0]} + soma({nums[1:]})")
        soma(nums[1:])

def potencia(n):
    nums = []
    for i in range(1, n+1):
        nums.append(2*i - 1)
    soma(nums)
    print('---------------')
    print(f'{n} ** 2 == {n**2}')

potencia(n)