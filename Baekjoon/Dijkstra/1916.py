import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))

start, end = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (n + 1)  # start로부터 다른 모든 노드까지의 거리
    queue = []

    heapq.heappush(queue, (0, start)) # (거리, 정점)
    distance[start] = 0

    while queue:
        dist, vertex = heapq.heappop(queue) # 최단 거리 노드 정보 반환
        if dist > distance[vertex]: # 기존 값보다 크면 패스
            continue

        for i in graph[vertex]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance[end]

print(dijkstra(start, end))
