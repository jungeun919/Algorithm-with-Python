# prim algorithm

# import heapq
# import sys

# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((c, b))
#     graph[b].append((c, a))

# visited = [False] * (n + 1)
# res = 0

# queue = []
# heapq.heappush(queue, (0, 1)) # (비용, 시작 노드)

# while queue:
#     weight, node = heapq.heappop(queue) # 첫번째 원소를 기준으로 정렬
    
#     if visited[node] == False:
#         visited[node] = True
#         res += weight
        
#         for next_weight, next_node in graph[node]:
#             heapq.heappush(queue, (next_weight, next_node))

# print(res)

# kruskal algorithm

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

graph.sort(key=lambda x : x[2])

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

res = 0

for a, b, cost in graph:
    # 사이클이 존재하지 않도록
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        res += cost

print(res)
