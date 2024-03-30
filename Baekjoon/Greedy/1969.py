import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dna = []
for _ in range(n):
    dna.append(input())

count = 0
res = ""

for i in range(m):
    acgt = [0, 0, 0, 0]
    
    for j in range(n):
        if dna[j][i] == 'A':
            acgt[0] += 1
        elif dna[j][i] == 'C':
            acgt[1] += 1
        elif dna[j][i] == 'G':
            acgt[2] += 1
        elif dna[j][i] == 'T':
            acgt[3] += 1
    
    idx = acgt.index(max(acgt))
    if idx == 0:
        res += 'A'
    elif idx == 1:
        res += 'C'
    elif idx == 2:
        res += 'G'
    elif idx == 3:
        res += 'T'
    
    count += n - max(acgt)

print(res)
print(count)
