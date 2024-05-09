from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    queue = deque()

    for v in range(1, N+1):
        if indegree[v] == 0:
            queue.append(v)

    res = []

    while queue:
        v = queue.popleft()
        res.append(v)

        for i in graph[v]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    for i in res:
        print(i, end=" ")

topology_sort()
