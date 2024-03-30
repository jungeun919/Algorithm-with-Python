from itertools import permutations
from copy import deepcopy
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

rotate = [] # 회전 연산 (r, c, s)
for _ in range(k):
    rotate.append(list(map(int, input().split())))

#     동  남  서  북
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

min_row = int(1e9)

# permutation(n, r): 서로 다른 n개 중 r개를 골라 순서 나열
for p in permutations(rotate, k):
    cp_arr = deepcopy(arr)

    for r, c, s in p:
        # 바깥 커브부터 회전
        for i in range(s):
            top_r, top_c = r-s+i-1, c-s+i-1 # 배열 좌표는 0부터 시작이므로 -1
            bottom_r, bottom_c = r+s-i-1, c+s-i-1

            y, x = top_r, top_c
            prev = cp_arr[y][x]

            for dir in range(4): # 네 변 확인
                while True:
                    ny = y + dy[dir]
                    nx = x + dx[dir]

                    if not(top_r <= ny <= bottom_r and top_c <= nx <= bottom_c):
                        break

                    cp_arr[ny][nx], prev = prev, cp_arr[ny][nx]
                    y, x = ny, nx

    # 모든 회전 연산 수행 후 최솟값 업데이트
    for row in cp_arr:
        min_row = min(min_row, sum(row))

print(min_row)
