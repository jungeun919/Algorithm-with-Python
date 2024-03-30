import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

plan = list(map(int, input().split()))

parent = [i for i in range(n)] # 자기자신을 부모로 초기화

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

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(i, j)

res = "YES"
for i in range(1, m):
    if parent[plan[i] - 1] != parent[plan[0] - 1]:
        res = "NO"
        break
print(res)
