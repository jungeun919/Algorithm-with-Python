from collections import deque
import sys

input = sys.stdin.readline

v = int(input())

tree = [[] for _ in range(v + 1)]
for _ in range(v):
	info = list(map(int, input().split()))
	for i in range(1, len(info) - 2, 2):
		tree[info[0]].append([info[i], info[i + 1]]) # [정점번호, 거리]

def bfs(start):
	visited = [0 for _ in range(v + 1)]

	queue = deque()
	queue.append([start, 0])
	visited[start] = 1

	max_node = start
	max_dist = 0

	while queue:
		node, dist = queue.popleft()
		if dist > max_dist:
			max_node = node
			max_dist = dist

		for n, d in tree[node]:
			if visited[n] == 0:
				queue.append([n, dist + d])
				visited[n] = 1
	return max_node, max_dist

temp_node, temp_dist = bfs(1)
res_node, res_dist = bfs(temp_node)
print(res_dist)
