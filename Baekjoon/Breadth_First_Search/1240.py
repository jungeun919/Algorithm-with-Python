from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

def bfs(a, b):
    queue = deque()
    queue.append((a, 0)) # 시작부터 해당 노드까지의 거리

    visited = [False] * (N+1)
    visited[a] = True

    while queue:
        node, dist = queue.popleft()
        if node == b:
            return dist

        for nv, d in graph[node]:
            if visited[nv] == False:
                queue.append((nv, dist + d))
                visited[nv] = True

for _ in range(M):
    a, b = map(int, input().split())
    print(bfs(a, b))
