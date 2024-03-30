# 맵의 행렬
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성
# 반복에 변수값이 필요 없을 때, _ 사용
d = [[0] * m for _ in range(n)]
# 현재 좌표, 방향
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
	array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
	global direction
	direction -= 1
	if direction == -1:
		direction = 3

count = 1
turn_time = 0
while True:
	turn_left()
	nx = x + dx[direction]
	ny = y + dy[direction]
	
	#가보지 않은 칸의 경우
	if d[nx][ny] == 0 and array[nx][ny] == 0:
		d[nx][ny] = 1
		x = nx
		y = ny
		count += 1
		turn_time = 0
		continue
	#가보지 않은 칸이 없거나 바다인 경우
	else:
		turn_time += 1
		
	if turn_time == 4:
		nx = x - dx[direction]
		ny = y - dy[direction]
		
		#뒤로 갈 수 있으면 이동
		if array[nx][ny] == 0:
			x = nx
			y = ny
		else:
			break
		turn_time = 0

print(count)
