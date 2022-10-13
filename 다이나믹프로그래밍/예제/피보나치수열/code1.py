# 재귀 이용 (top-down)
d = [0] * 100

def fibo(x):
	if x == 1 or x == 2:
		return 1
	
	# 이미 계산한 적 있는 문제
	if d[x] != 0:
		return d[x]

	d[x] = fibo(x - 1) + fibo(x - 2)
	return d[x]

print(fibo(99))
