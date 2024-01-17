# k를 거쳐가는 경로 구하기
import sys

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
	graph.append(list(input().rstrip()))

# 2-친구 관계
relation = [[0] * n for _ in range(n)]

for k in range(n):
	for i in range(n):
		for j in range(n):
			if i == j:
				continue

			if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
				relation[i][j] = True

max_friend = 0
for row in relation:
	max_friend = max(max_friend, sum(row))
print(max_friend)
