from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                queue.append(i)

bfs(start)

if visited[end] > 0:
    print(visited[end])
else:
    print(-1)
