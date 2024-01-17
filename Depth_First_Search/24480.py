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
    graph[i].sort(reverse=True)
    
visited = [False] * (n + 1)
visited[start] = True

result = [0] * (n + 1)

count = 1
def dfs(n):
    global count
    result[n] = count
    visited[n] = True
    
    for i in graph[n]:
        if visited[i] == False:
            count += 1
            dfs(i)
            
dfs(start)

for i in result[1:]:
    print(i)
