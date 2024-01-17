import sys

input = sys.stdin.readline

s = input()

alpha = [[0] * 26 for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    for j in range(26):
        if ord(s[i - 1]) - 97 == j:
            alpha[i][j] = alpha[i - 1][j] + 1
        else:
            alpha[i][j] = alpha[i - 1][j]

q = int(input())
for _ in range(q):
    char, left, right = input().split()
    char, left, right = ord(char) - 97, int(left), int(right)

    print(alpha[right + 1][char] - alpha[left][char])
