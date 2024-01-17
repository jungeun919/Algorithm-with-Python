from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)] # 1부터 시작
for _ in range(m):
	u, v = map(int, input().split())
	# 무방향
	graph[u].append(v)
	graph[v].append(u)

def bfs(start):
	queue = deque()
	queue.append(start)
	visited[start] = True

	while queue:
		v = queue.popleft()
		for i in graph[v]:
			if visited[i] == False:
				queue.append(i)
				visited[i] = True

count = 0
visited = [False] * (n + 1)

for i in range(1, n + 1):
	if visited[i] == False:
		bfs(i)
		count += 1

print(count)
