n = int(input())
len_n = len(str(n))

res = 0
for i in range(len_n - 1):
	res += 9 * (10 ** i) * (i + 1)
res += (n - (10 ** len_n - 1) + 1) * len_n
print(res)
