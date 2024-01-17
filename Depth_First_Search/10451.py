import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

T = int(input())

def dfs(v):
	visited[v] = True
	next_v = nums[v]
	if not visited[next_v]:
		dfs(next_v)

for _ in range(T):
	n = int(input())
	nums = [0] + list(map(int, input().split()))

	visited = [0] * (n + 1)
	count = 0

	for i in range(1, n + 1):
		if not visited[i]:
			dfs(i)
			count += 1
	print(count)
