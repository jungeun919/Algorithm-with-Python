# 간단한 다익스트라 알고리즘 : 시간복잡도 -> O(노드 수 ^ 2)
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한 -> 10억으로 설정

n, m = map(int, input().split()) # 노드 수, 간선 수
start = int(input()) # 시작 노드

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a -> b 노드로 가는 비용이 c
    graph[a].append((b, c))
    
print("graph:", graph)

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드 인덱스 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    
    for i in graph[start]:
        distance[i[0]] = i[1]
        
	# 시작 노드(start) 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        
		# 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
