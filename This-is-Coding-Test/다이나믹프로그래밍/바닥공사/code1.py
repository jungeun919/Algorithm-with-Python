# bottom-up
# 가로 길이 : n, 세로 길이 : 2
# 2 * n 크기의 바닥을 채우는 방법의 수를 796796으로 나눈 나머지 출력하기
n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n + 1):
	d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])
