from collections import deque
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

tree = []
for row in range(N):
    tree.append([deque() for _ in range(N)])

for _ in range(M):
    x, y, z = map(int, input().split()) # (x, y) 위치, z 나이
    tree[x-1][y-1].append(z)

nutrient = [[5] * N for _ in range(N)]

def spring_summer():
    for i in range(N):
        for j in range(N):
            tree_count = len(tree[i][j])
            for k in range(tree_count):
                if nutrient[i][j] >= tree[i][j][k]:
                    nutrient[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    for _ in range(k, tree_count):
                        age = tree[i][j].pop()
                        nutrient[i][j] += age//2
                    break

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def fall_winter():
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for d in range(8):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            tree[nx][ny].appendleft(1)

            nutrient[i][j] += board[i][j]

for _ in range(K):
    spring_summer()
    fall_winter()

count = 0
for i in range(N):
    for j in range(N):
        count += len(tree[i][j])
print(count)
