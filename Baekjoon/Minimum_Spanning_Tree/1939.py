import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n + 1)] # 자기자신을 부모로 초기화

def find_parent(node):
	if node != parent[node]:
		parent[node] = find_parent(parent[node])
	return parent[node]

def union_parent(x, y):
	x = find_parent(x)
	y = find_parent(y)

	if x > y: # 작은 쪽이 부모로
		parent[x] = y
	else:
		parent[y] = x

graph = []
for _ in range(m):
	a, b, limit = map(int, input().split())
	graph.append([limit, a, b])

graph.sort(key=lambda x : x[0], reverse=True)

p, q = map(int, input().split())

for limit, a, b in graph:
	# 사이클이 존재하지 않도록
	if find_parent(a) != find_parent(b):
		union_parent(a, b)

		if find_parent(p) == find_parent(q):
			print(limit)
			break
