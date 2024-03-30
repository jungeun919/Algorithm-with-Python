from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0] * 100001 # 방문 여부, 시간 저장

def bfs(start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        
        if v == k:
            return visited[v]
        
        for nv in (v - 1, v + 1, 2 * v):
            if 0 <= nv < 100001 and visited[nv] == 0:
                visited[nv] = visited[v] + 1
                queue.append(nv)
           
print(bfs(n))
