from collections import deque
import sys

input = sys.stdin.readline

# 빈 칸: 0
# 뱀: 1
# 사과: 2
n = int(input())
board = [[0] * n for _ in range(n)]

k = int(input()) # 사과의 개수
for _ in range(k):
	r, c = map(int, input().split())
	board[r-1][c-1] = 2

l = int(input()) # 방향 변환 횟수
change = dict()
for _ in range(l):
	time, dir = input().split()
	change[int(time)] = dir

#     동  남  서  북
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def turn(alpha):
	global dir

	if alpha == 'L':
		# 왼쪽으로 90도 회전
		dir = (dir - 1) % 4
	elif alpha == 'D':
		# 오른쪽으로 90도 회전
		dir = (dir + 1) % 4

board[0][0] = 1 # 시작 위치
y, x = 0, 0 # 시작 행, 열 초기화
dir = 0 # 오른쪽 방향부터 시작
time = 0 # 진행 시간

snake = deque() # 뱀의 위치
snake.append([0, 0])

while True:
	time += 1

	x += dx[dir]
	y += dy[dir]

	if not(0 <= y < n and 0 <= x < n):
		break

	if board[y][x] == 1: # 자기자신의 몸과 부딪혔을 때
		break

	elif board[y][x] == 2:
		# 몸길이 늘리기
		board[y][x] = 1
		snake.append([y, x])
	
	elif board[y][x] == 0:
		# 몸길이 늘리기
		board[y][x] = 1
		snake.append([y, x])
		# 꼬리 비우기
		tail_y, tail_x = snake.popleft()
		board[tail_y][tail_x] = 0
	
	# 방향 전환 정보 확인
	if time in change:
		turn(change[time])

print(time)
