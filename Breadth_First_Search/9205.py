from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
	n = int(input())

	home = list(map(int, input().split()))
	store = []
	for _ in range(n):
		store.append(list(map(int, input().split())))
	festival = list(map(int, input().split()))

	# bfs
	visited = [False] * n # 편의점 방문, 1부터 시작
	res = False
	
	queue = deque()
	queue.append([home[0], home[1]])

	while queue:
		x, y = queue.popleft()

		if abs(x - festival[0]) + abs(y - festival[1]) <= 1000: # 20병 * 50미터
			res = True
			break

		for i in range(n):
			if visited[i] == False:
				store_x, store_y = store[i]
				if abs(x - store_x) + abs(y - store_y) <= 1000:
					visited[i] = True
					queue.append([store_x, store_y])
		
	if res == True:
		print("happy")
	else:
		print("sad")
