dna1 = input()
dna2 = input()

dna1_size = len(dna1)
dna2_size = len(dna2)
maior = 0

def seqComum(dna1, dna2, i, j):
    if i >= len(dna1) or j >= len(dna2):
        return 0
    if dna1[i] == dna2[j]:
        return 1 + seqComum(dna1,dna2, i+1, j+1)
    else:
        return 0

for i in range(dna1_size):
    for j in range(dna2_size):
        n = seqComum(dna1, dna2, i, j)
        if n > maior:
            maior = n

print(dna1_size)
print(dna2_size)
print(maior)