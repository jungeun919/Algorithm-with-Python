n = int(input())
check = list(map(int, input().split()))

res = [0] * n

for i in range(n): # 작은 수부터 채워나가기
	count = 0 # 왼쪽에 자기보다 큰 사람 수
	for j in range(n):
		if check[i] == count and res[j] == 0:
			res[j] = i + 1
			break
		elif res[j] == 0:
			count += 1

for i in res:
	print(i, end=" ")
