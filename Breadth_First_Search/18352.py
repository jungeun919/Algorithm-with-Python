from collections import deque
import sys

input = sys.stdin.readline

n, m, dist, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)

def bfs(start):
    queue = deque([start])
    distance[start] = 0
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if distance[i] == -1:
                distance[i] = distance[v] + 1
                queue.append(i)

bfs(start)

flag = False
for i in range(1, n + 1):
    if distance[i] == dist:
        flag = True
        print(i)
if flag == False:
    print(-1)
