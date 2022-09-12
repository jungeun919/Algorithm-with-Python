# 탐색

* 대표적인 탐색 알고리즘이 dfs/bfs
* 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 의미함

# 자료구조

* 데이터를 표현하고 관리하고 처리하기 위한 구조를 의미함
* 스택 (stack)
	* 선입후출 / 후입선출 구조
* 큐 (queue)
	* 선입선출 구조
	* 큐를 구현할 때 collections 모듈에서 제공하는 deque 자료구조 활용
* 제귀함수 (recusive function)
	* 자기 자신을 다시 호출하는 함수
	* 함수 종료 조건을 반드시 명시 -> 그렇지 않을 경우 무한 루프

# 그래프

* 용어 : 노드(정점) / 간선
* 그레프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말함
* 인접 행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
* 인접 리스트 : 리스트로 그래프의 연결 관계를 표현하는 방식

# DFS (Depth-First-Search)

* 깊이 우선 탐색
* 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
* 스택 자료구조를 이용

```python
graph = [
	[], 
	[2, 3, 8],
	[1, 7], 
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

visited = [False] * 9

def dfs(graph, v, visited):
	visited[v] = True
	print(v, end = ' ')

	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

dfs(graph, 1, visited)
```

# BFS (Breadth-First-Search)

* 너비 우선 탐색
* 가까운 노드부터 탐색하는 알고리즘
* 큐 자료구조를 이용

```python
from collections import deque

graph = [
	[], 
	[2, 3, 8],
	[1, 7], 
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

visited = [False] * 9

def bfs(graph, start, visited):
	queue = deque([start])
	visited[start] = True
	
	while queue:
		v = queue.popleft()
		print(v, end = ' ')
		
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

bfs(graph, 1, visited)
```
