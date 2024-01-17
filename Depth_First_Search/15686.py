import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n):
	board.append(list(map(int, input().split())))

# 정보 저장
houses = []
chickens = []
for row in range(n):
	for col in range(n):
		if board[row][col] == 1:
			houses.append([row, col])
		elif board[row][col] == 2:
			chickens.append([row, col])

def dfs(arr, idx):
	global res
	
	# 조합 완료
	if len(arr) == m:
		# 치킨 거리 계산
		total_dist = 0
		for house in houses:
			dist = 100 # max_dist
			for chicken in arr:
				dist = min(dist, \
					abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
			total_dist += dist
		
		res = min(res, total_dist)
		return
	
	if idx == len(chickens): # 조합 불가능
		return
	
	# 조합 생성
	arr.append(chickens[idx])
	dfs(arr, idx + 1)
	arr.pop()
	dfs(arr, idx + 1)

res = 100 * 13 # max_dist * max_chicken
dfs([], 0)
print(res)
