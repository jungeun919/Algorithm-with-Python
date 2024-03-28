import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, time = map(int, input().split())
    graph[a].append((b, time))

def dijkstra(start, end):
    distance = [INF] * (n+1) # start로부터 다른 모든 노드까지의 거리
    queue = []

    heapq.heappush(queue, (0, start)) # (거리, 정점)
    distance[start] = 0

    while queue:
        dist, vertex = heapq.heappop(queue)
        if dist > distance[vertex]:
            continue

        for i in graph[vertex]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance[end]

max_time = 0
for i in range(1, n+1):
    if i == x:
        continue

    path1 = dijkstra(i, x)
    path2 = dijkstra(x, i)
    max_time = max(max_time, path1 + path2)
print(max_time)
