import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split()) # 지역, 수색 범위, 길의 개수

items = [0] + list(map(int, input().split()))

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
	graph[i][i] = 0

for _ in range(r):
	a, b, l = map(int, input().split())
	graph[a][b] = l
	graph[b][a] = l

for k in range(1, n+1):
	for i in range(1, n+1):
		for j in range(1, n+1):
			graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

max_count = 0
for i in range(1, n+1):
	count = 0
	for j in range(1, n+1):
		if graph[i][j] <= m:
			count += items[j]
	max_count = max(max_count, count)
print(max_count)
