N = int(input())

graph = [[] for _ in range(N+1)]
for idx in range(1, N+1):
    v = int(input())
    graph[v].append(idx)

def dfs(v, i): # 현재 노드, 시작한 노드
    visited[v] = True

    for nv in graph[v]:
        if visited[nv] == False:
            dfs(nv, i)
        elif visited[nv] == True and nv == i:
            res.append(nv)

res = []
for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i, i)

print(len(res))
res.sort()
for i in res:
    print(i)
