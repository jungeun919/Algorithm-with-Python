# 음수 * 음수 / 양수 * 양수
# 절댓값이 큰 수끼리 곱셈

n = int(input())

pos = []
neg = []
one = 0 # 곱셈보다 덧셈으로 처리하는 것이 유리
zero = 0 # 음수가 홀수 개일 경우 0 곱해주기

for _ in range(n):
	num = int(input())
	if num > 1:
		pos.append(num)
	elif num < 0:
		neg.append(num)
	elif num == 1:
		one += 1
	else:
		zero = 1

pos.sort()
neg.sort(reverse=True)

total = 0

while len(pos) >= 2:
	total += pos.pop() * pos.pop()

if pos:
	total += pos.pop()

while len(neg) >= 2:
	total += neg.pop() * neg.pop()

if neg:
	if zero:
		# total += neg.pop() * 0
		pass
	else:
		total += neg.pop()

total += one

print(total)
