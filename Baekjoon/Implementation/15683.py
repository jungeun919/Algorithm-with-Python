import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 0 | 빈 칸
# 1~5 | cctv
# 6 | 벽
info = []
for _ in range(n):
	info.append(list(map(int, input().split())))

# 각 cctv가 감시할 수 있는 방향
dir_cases = {
	1: [[0], [1], [2], [3]],
	2: [[0, 2], [1, 3]],
	3: [[0, 1], [1, 2], [2, 3], [3, 0]],
	4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
	5: [[0, 1, 2, 3]]
}

cctv = []
for r in range(n):
	for c in range(m):
		if info[r][c] in [1, 2, 3, 4, 5]:
			cctv.append([info[r][c], r, c])

#     상  하  좌  우
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# 90씩 회전한 방향
#     동  서  남  북
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def print_info(info):
	print('print')
	for r in range(n):
		print(' '.join(map(str, info[r])))
	print('----------')

def zero_count(info):
	count = 0
	for row in info:
		count += row.count(0)
	return count

def move(y, x, info, dir_case):
	for i in dir_case:
		ny = y
		nx = x

		while True:
			ny += dy[i]
			nx += dx[i]

			if not(0 <= ny < n and 0 <= nx < m):
				break
			if info[ny][nx] == 6:
				break
			if info[ny][nx] == 0:
				info[ny][nx] = '#'

def dfs(depth, info):
	global min_count

	if depth == len(cctv):
		count = zero_count(info)
		min_count = min(min_count, count)
		return
	
	cctv_num, y, x = cctv[depth]

	for dir_case in dir_cases[cctv_num]:
		cp_info = [[j for j in info[i]] for i in range(n)]
		move(y, x, cp_info, dir_case)
		dfs(depth + 1, cp_info)

min_count = int(1e9)
dfs(0, info)
print(min_count)
