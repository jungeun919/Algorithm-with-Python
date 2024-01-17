import sys

input = sys.stdin.readline

v, e = map(int, input().split())

graph = []
for _ in range(e):
    graph.append(list(map(int, input().split())))

graph.sort(key=lambda x : x[2])

parent = [i for i in range(v + 1)] # 자기자신을 부모로 초기화

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

res = 0

for a, b, cost in graph:
    # 사이클이 존재하지 않도록
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        res += cost

print(res)
