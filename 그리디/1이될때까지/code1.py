# n : 1로 만들 수
# k : 나눌 수
n, k = map(int, input().split())
result = 0

while n >= k:
	while n % k != 0:
		n -= 1
		result += 1
	n = n // k
	result += 1

while n > 1:
	n -= 1
	result += 1

print(result)
