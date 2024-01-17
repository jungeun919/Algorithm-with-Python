import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

T = int(input())

def dfs(v):
	global res

	visited[v] = True
	cycle.append(v)
	next_v = select[v]

	if visited[next_v] != 0:
		if next_v in cycle:
			res += cycle[cycle.index(next_v):]
		return
	else:
		dfs(next_v)

for _ in range(T):
	n = int(input())
	select = [0] + list(map(int, input().split()))

	visited = [0] * (n + 1)
	res = []

	for i in range(1, n + 1):
		if not visited[i]:
			cycle = []
			dfs(i)
	
	print(n - len(res))
