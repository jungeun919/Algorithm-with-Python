# 다익스트라 알고리즘 (우선순위 큐)

# n : 도시의 개수
# m : 통로의 개수
# start : 시작 도시
# x, y, z : x에서 y로 가는 비용 z

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

# 각 간선에 대한 정보 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    
def dijkstra(start):
    q = []
    
    heapq.heappush(q, (0, start)) # (거리, 노드)
    distance[start] = 0
    
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q) # 최단 거리 노드 정보 꺼내기
        # 이미 처리된 적이 있는 노드일 경우 무시
        if distance[now] < dist:
            continue
        
		# 현재 노드와 연결된 다른 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
        
# 시작 노드 제외
print(count - 1, max_distance)
