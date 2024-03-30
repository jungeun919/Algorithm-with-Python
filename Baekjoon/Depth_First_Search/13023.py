import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n
res = 0

def dfs(idx, depth):
    global res
    
    if depth == 4:
        res = 1
        return
    
    for i in graph[idx]:
        if visited[i] == False:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
    
    if res == 1: # 하나라도 ok
        break

print(res)
