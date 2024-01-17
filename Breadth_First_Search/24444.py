from collections import deque
import sys

input = sys.stdin.readline

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n + 1):
    graph[i].sort()
    
visited = [False] * (n + 1)
result = [0] * (n + 1)

def bfs(start):
    count = 1
    visited[start] = True
    result[start] = count
    
    queue = deque([start]) # deque([1])
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if visited[i] == False:
                count += 1
                result[i] = count
                queue.append(i) # deque([2, 4])
                visited[i] = True
                
bfs(start)

for i in result[1:]:
    print(i)
