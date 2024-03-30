# 다음과 같이 노드의 연결 관계가 그래프 형태로 주어집니다. 그 다음 경로를 구할 두 정점이 공백으로 구분되어 주어질 것입니다. 

# 두 정점 사이를 이동할 수 있는 최단거리를 출력하는 프로그램을 작성해 주세요. 

# 이 때 최단 거리란, 정점의 중복 없이 한 정점에서 다른 정점까지 갈 수 있는 가장 적은 간선의 수를 의미합니다.

# >> 입력 : A F
# >> 출력 : 2

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

start, end = [i for i in input().split()]
    
queue = [start]
visited = [start]
    
def solution():
    count = -1

    while len(queue) != 0:
        count += 1
        size = len(queue)

        for i in range(size):
            node = queue.pop(0)
            if node == end:
                return count

            for next_node in graph[node]:
                if next_node not in visited:
                    visited.append(next_node)
                    queue.append(next_node)

print(solution())