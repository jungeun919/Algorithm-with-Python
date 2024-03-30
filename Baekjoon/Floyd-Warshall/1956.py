import sys

input = sys.stdin.readline
INF = int(1e9)

node, edge = map(int, input().split())

graph = [[INF] * (node + 1) for _ in range(node + 1)]

for _ in range(edge):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, node + 1):
    for a in range(1, node + 1):
        for b in range(1, node + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

res = INF
for i in range(1, node + 1):
    res = min(res, graph[i][i])

if res == INF:
    print(-1)
else:
    print(res)
