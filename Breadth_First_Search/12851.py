from collections import deque

n, k = map(int, input().split())

visited = [-1] * 100001 # 방문 여부, 시간 저장
count = 0 # 경우의 수

queue = deque([n])
visited[n] = 0

while queue:
    v = queue.popleft()
    
    if v == k:
        count += 1
        
    for next_v in (v - 1, v + 1, 2 * v):
        if 0 <= next_v <= 100000:
            # 처음 방문 or 가장 빠른 시간이 있는 경우
            if visited[next_v] == -1 or visited[next_v] >= visited[v] + 1:
                visited[next_v] = visited[v] + 1
                queue.append(next_v)

print(visited[k])
print(count)
