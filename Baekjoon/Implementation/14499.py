import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

dice = []
for _ in range(n):
	dice.append(list(map(int, input().split())))

# 동(1) 서(2) 북(3) 남(4)
commands = list(map(int, input().split()))

#     동  서  북  남
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(k):
	print(commands[i], end=" ")
