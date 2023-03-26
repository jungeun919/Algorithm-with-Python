# 개선된 다익스트라 알고리즘 : 시간복잡도 -> O(간선 수 * log 노드 수)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한 -> 10억으로 설정

n, m = map(int, input().split()) # 노드 수, 간선 수
start = int(input()) # 시작 노드

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a -> b 노드로 가는 비용이 c
    graph[a].append((b, c))
    
print("graph:", graph)

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

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
