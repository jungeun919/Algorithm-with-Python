import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

node, edge = map(int, input().split())

graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))

pass1, pass2 = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (node + 1)
    queue = []

    heapq.heappush(queue, (0, start)) # 거리, 정점
    distance[start] = 0
    
    while queue:
        dist, vertex = heapq.heappop(queue) # 최단 거리 노드 정보 반환
        if distance[vertex] < dist:
            continue

        for i in graph[vertex]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    
    return distance[end]

path1 = dijkstra(1, pass1) + dijkstra(pass1, pass2) + dijkstra(pass2, node)
path2 = dijkstra(1, pass2) + dijkstra(pass2, pass1) + dijkstra(pass1, node)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))
