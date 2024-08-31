from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # 노드, 간선

graph = [[] for _ in range(N+1)]
for _ in range(M):
	a, b = map(int, input().split()) # a가 b를 신뢰
	graph[b].append(a)

def bfs(start):
	queue = deque()
	queue.append(start)

	visited = [False] * (N+1)
	visited[start] = True

	count = 0
	while queue:
		v = queue.popleft()

		for i in graph[v]:
			if visited[i] == False:
				queue.append(i)
				visited[i] = True
				count += 1
	return count

res = []
for i in range(1, N+1):
	res.append(bfs(i))

for i in range(N):
	if max(res) == res[i]:
		print(i+1, end=" ")
