# 너비 우선 탐색이란 어떤 노드를 방문하여 확인 한 후, 목표한 노드가 아니면 그 노드와 연결된 정점들 중에서 우선순위가 동일한 다른 노드를 찾고 그 순위에 없으면 그 다음 순위 노드를 차례대로 찾는 방법이다.

# 다음과 같이 입력이 주어질 때 너비 우선 탐색을 한 순서대로 노드의 인덱스를 공백 구분으로 출력하는 프로그램을 완성해주세요.

# 1. 데이터
# graph = {'E': set(['D', 'A']),
#          'F': set(['D']),
#          'A': set(['E', 'C', 'B']),
#          'B': set(['A']),
#          'C': set(['A']),
#          'D': set(['E','F'])}

# 2. 출력
# ['E', 'D', 'A', 'F', 'C', 'B']

# 3. 코드
graph = {'E': set(['D', 'A']),
         'F': set(['D']),
         'A': set(['E', 'C', 'B']),
         'B': set(['A']),
         'C': set(['A']),
         'D': set(['E','F'])}

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

print(bfs(graph, 'E'))