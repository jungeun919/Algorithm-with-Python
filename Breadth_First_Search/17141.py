# 0 : 빈 칸
# 1 : 벽
# 2 : 바이러스
# m : 바이러스 개수

from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
virus = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

for row in range(n):
    for col in range(n):
        if graph[row][col] == 2:
            virus.append((row, col))

#     상  하  좌  우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    queue = deque()
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            


for v in combinations(virus, m):
    min_time = min(bfs(v), min_time)

if min_time == "inf":
    print(-1)
else:
    print(min_time)
