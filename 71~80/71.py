# 깊이 우선 탐색이란 목표한 노드를 찾기 위해 가장 우선순위가 높은 노드의 자식으로 깊이 들어 갔다가 목표 노드가 존재하지 않으면 처음 방문한 노드와 연결된 다른 노드부터 그 자식 노드로 파고드는 검색 방법을 말합니다.

# 다음과 같이 리스트 형태로 노드들의 연결 관계가 주어진다고 할 때 깊이 우선 탐색으로 이 노드들을 탐색했을 때의 순서를 공백으로 구분하여 출력하는 프로그램을 완성하세요.

# 1. 데이터
# graph = {'E': set(['D', 'A']),
#          'F': set(['D']),
#          'A': set(['E', 'C', 'B']),
#          'B': set(['A']),
#          'C': set(['A']),
#          'D': set(['E','F'])}

# 2. 출력
# ['E', 'A', 'B', 'C', 'D', 'F']

# 3. 코드
graph = {
        'A': set(['B', 'C', 'E']),
        'B': set(['A']),
        'C': set(['A']),
        'D': set(['E', 'F']),
        'E': set(['A', 'D']),
        'F': set(['D'])
}

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
            print(stack)
    return visited

print(dfs(graph, 'E'))