# n개의 원소, k번 바꿔치기
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
	if a[i] < b[i]:
		a[i], b[i] = b[i], a[i]
	else:
		break

print(sum(a))
