from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n + 1):
    graph[i].sort()

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    visited[start] = True
    
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                
visited = [False] * (n + 1)
dfs(start)
print()
visited = [False] * (n + 1)
bfs(start)
