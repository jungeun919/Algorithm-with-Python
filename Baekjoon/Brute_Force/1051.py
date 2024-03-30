import sys

input = sys.stdin.readline

n, m = map(int, input().split())

square = []
for _ in range(n):
	square.append(list(map(int, input().rstrip())))

size = min(n, m) # 밑변의 길이

for i in range(size, 0, -1): # 한변길이: size ~ 1
	for row in range(n - i + 1): # 0 ~ (가로-한변길이)
		for col in range(m - i + 1): # 0 ~ (세로-한변길이)
			if square[row][col] == square[row][col + i - 1] == square[row + i - 1][col] == square[row + i - 1][col + i - 1]:
				print(i ** 2)
				exit(0)
