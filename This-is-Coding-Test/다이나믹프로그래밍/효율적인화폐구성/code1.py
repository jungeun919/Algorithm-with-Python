# bottom-up
# n : 화폐의 종류
# m : 가치의 합
# array : 화폐 단위 정보
# m원을 만들기 위한 최소한의 화폐 개수 출력하기 (불가능할 때는 -1 출력)
n, m = map(int, input().split())

array = []
for i in range(n):
	array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
	for j in range(array[i], m + 1):
		if d[j - array[i]] != 10001:
			d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
	print(-1)
else:
	print(d[m])
