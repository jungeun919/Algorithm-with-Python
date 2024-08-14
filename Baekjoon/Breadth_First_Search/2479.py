from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split()) # 길이가 K인 N개의 이진 코드

code = [None]
for i in range(1, N+1):
	code.append(input().rstrip())

s, e = map(int, input().split())

def hamming_dist(a, b):
	dist = 0
	for i in range(K):
		if a[i] != b[i]:
			dist += 1
	return dist

def get_path(s, e):
	queue = deque()
	queue.append([s, [s]])

	visited = [False] * (N+1)
	visited[s] = True

	while queue:
		num, path = queue.popleft()
		if num == e:
			str_path = " ".join(map(str, path))
			return str_path
		
		for i in range(1, N+1):
			if visited[i] == False:
				if hamming_dist(code[num], code[i]) == 1:
					visited[i] = True
					queue.append([i, path + [i]])
	
	return -1

print(get_path(s, e))
