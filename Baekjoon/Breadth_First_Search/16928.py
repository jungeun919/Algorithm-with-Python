from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # 사다리 수, 뱀 수

ladder = dict()
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

snake = dict()
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

def bfs(start):
    visited = [False] * 101

    queue = deque()
    queue.append([start, 0]) # [현재 위치, 주사위 횟수]

    while queue:
        v, count = queue.popleft()
        if v == 100:
            print(count)
            break

        for i in range(1, 7):
            nv = v + i
            if nv <= 100 and visited[nv] == False:
                visited[nv] = True
                if nv in ladder.keys():
                    queue.append([ladder[nv], count + 1])
                elif nv in snake.keys():
                    queue.append([snake[nv], count + 1])
                else:
                    queue.append([nv, count + 1])

# 1에서 100까지 이동하기
bfs(1)
