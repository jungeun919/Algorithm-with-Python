import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

node, edge = map(int, input().split())
start = int(input())

graph = [[] for _ in range(node + 1)]
distance = [INF] * (node + 1)

for _ in range(edge):
    begin, end, weight = map(int, input().split())
    graph[begin].append((end, weight))

def dijkstra(start):
    queue = []
    
    heapq.heappush(queue, (0, start)) # (거리, 정점)
    distance[start] = 0
    
    while queue:
        dist, vertex = heapq.heappop(queue) # 최단 거리 노드 정보 반환
        if distance[vertex] < dist:
            continue
        
        for i in graph[vertex]:
            cost = dist + i[1]
            if cost < distance[i[0]]: # 최단 경로 업데이트
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)

for d in distance[1:]:
    if d == INF:
        print("INF")
    else:
        print(d)
