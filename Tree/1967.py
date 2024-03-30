import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append([child, weight])
    tree[child].append([parent, weight])

def dfs(vertex, weight):
    for nv, nw in tree[vertex]:
        if visited[nv] == -1:
            visited[nv] = weight + nw
            dfs(nv, weight + nw)

visited = [-1] * (n+1) # 방문 여부, 루트 노드(1)로부터 다른 모든 노드까지의 거리
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))

visited = [-1] * (n+1) # 방문 여부, start 노드로부터 다른 모든 노드까지의 거리
visited[start] = 0
dfs(start, 0)

print(max(visited))
