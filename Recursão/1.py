rec1, rec2 = map(int, input().split())

def mmc(num1, num2):
    d = min(num1,num2)
    while  (num1 % d) or (num2 % d):
        d -= 1
        if d == 0:
            break
    return d

print(mmc(rec1, rec2))