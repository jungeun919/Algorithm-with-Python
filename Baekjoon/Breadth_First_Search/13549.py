# 1초 후 : x-1 or x+1
# 0초 후 : 2*x

from collections import deque

n, k = map(int, input().split())

visited = [-1] * 100001 # 방문 여부, 시간 저장

queue = deque([n])
visited[n] = 0

while queue:
    v = queue.popleft()
    
    if v == k:
        print(visited[k])
        break
    
    if 0 <= 2 * v <= 100000 and visited[2 * v] == -1:
        visited[2 * v] = visited[v]
        queue.appendleft(2 * v) # 더 높은 우선순위 적용
    if 0 <= v - 1 <= 100000 and visited[v - 1] == -1:
        visited[v - 1] = visited[v] + 1
        queue.append(v - 1)
    if 0 <= v + 1 <= 100000 and visited[v + 1] == -1:
        visited[v + 1] = visited[v] + 1
        queue.append(v + 1)
