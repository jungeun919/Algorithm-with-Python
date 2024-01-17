import sys

input = sys.stdin.readline


#     북          동
#   서   동 =>  북   남
#     남          서

# d: [0, 1, 2, 3] = [북, 동, 남, 서]
# 반시계방향: [0, 3, 2, 1] = [북, 서, 남, 동]
# 왼쪽으로 회전 [3, 2, 1, 0] = [서, 남, 동, 북]
# (d + 3) % 4

n, m = map(int, input().split())
r, c, d = map(int, input().split())

# (i, j): [0, 1] = [빈 칸, 벽]
board = []
for _ in range(n):
	board.append(list(map(int, input().split())))

#     북  동  남  서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited = [[0] * m for _ in range(n)]

# 현재 칸 청소
visited[r][c] = 1
count = 1

while True:
	flag = False

	# 주변 4방향 탐색
	for _ in range(4):
		# 왼쪽으로 회전
		d = (d + 3) % 4
		nr = r + dr[d]
		nc = c + dc[d]

		if 0 <= nr < n and 0 <= nc < m:
			if board[nr][nc] == 0 and visited[nr][nc] == 0:
				visited[nr][nc] = 1
				count += 1
				r, c, = nr, nc
				flag = True
				break
	
	if flag == False:
		# 후진
		if board[r - dr[d]][c - dc[d]] == 0:
			r -= dr[d]
			c -= dc[d]
		else:
			break

print(count)
