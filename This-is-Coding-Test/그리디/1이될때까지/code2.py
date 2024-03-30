# n : 1로 만들 수
# k : 나눌 수
n, k = map(int, input().split())
result = 0

while True:
	target = (n // k) * k
	result += (n - target)

	n = target
	if n < k:
		break
	
	result += 1
	n = n // k

result += (n - 1)
print(result)
