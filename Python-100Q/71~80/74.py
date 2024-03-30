# 첫 줄에는 다음과 같은 집합 자료형 형태로 노드의 연결 관계가 주어집니다. 
# 두번째 줄에는 경로를 구할 두 정점의 번호가 공백으로 구분되어 주어집니다.
# 이 두 정점으로 가기 위한 최대 거리를 구하고자 합니다. 

# 최대 거리란, 정점의 중복 없이 한 정점에서 다른 정점까지 경유할 수 있는 가장 많은 간선의 수를 뜻합니다.

# >> 입력
# 1 7
# >> 출력
# 6

graph = {
    1: [2, 3, 4],
	2: [1, 3, 4, 5, 6],
	3: [1, 2, 7],
	4: [1, 2, 5, 6],
	5: [2, 4, 6, 7],
	6: [2, 4, 5, 7],
	7: [3, 5, 6]
} 

start, end = [int(i) for i in input().split()]
queue = [start]
visited = []

def sol(n, visited):
	if n[-1] == end:
		return len(visited)
	
	if n[-1] in visited:
		return len(visited)
	
	visited.append(n[-1])
	length = 0
	
	for next_node in graph[n[-1]]:
		n.append(next_node)
		length = max(length, sol(n, visited))
		queue.pop(-1)
	return length

print(sol(queue, visited))