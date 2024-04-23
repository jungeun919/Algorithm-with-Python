import sys

input = sys.stdin.readline

n = int(input())

A = []
B = []
C = []
D = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AplusB = []
for a in A:
    for b in B:
        AplusB.append(a+b)

CplusD = []
for c in C:
    for d in D:
        CplusD.append(c+d)

AplusB.sort()
CplusD.sort()

left, right = 0, len(CplusD) - 1
res = 0

while left < len(AplusB) and right >= 0:
    temp = AplusB[left] + CplusD[right]
    if temp < 0:
        left += 1
    elif temp > 0:
        right -= 1
    else:
        # AplusB에서 중복된 개수 체크
        checkAB = 1
        while left + checkAB < len(AplusB) and AplusB[left] == AplusB[left + checkAB]:
            checkAB += 1

        # CplusD에서 중복된 개수 체크
        checkCD = 1
        while right - checkCD >= 0 and CplusD[right] == CplusD[right - checkCD]:
            checkCD += 1

        res += checkAB * checkCD
        left += checkAB
        right += checkCD

print(res)
