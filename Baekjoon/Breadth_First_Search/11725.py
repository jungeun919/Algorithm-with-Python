from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

res = [0] * (n + 1)

def bfs(start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if res[i] == 0:
                res[i] = v
                queue.append(i)

bfs(1)

for i in res[2:]:
    print(i)
