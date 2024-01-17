import sys

input = sys.stdin.readline

n = int(input())

count = 0

for _ in range(n):
	word = input().rstrip()
	stack = []

	for i in range(len(word)):
		if stack and word[i] == stack[-1]:
			stack.pop()
		else:
			stack.append(word[i])
	
	if not stack:
		count += 1

print(count)
