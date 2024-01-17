import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

node = int(input())
edge = int(input())

graph = [[] for _ in range(node + 1)]
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

visited = [False] * (node + 1)

count = 0
def dfs(v):
    global count
    visited[v] = True
    
    for i in graph[v]:
        if visited[i] == False:
            count += 1
            dfs(i)

dfs(1)

print(count)
