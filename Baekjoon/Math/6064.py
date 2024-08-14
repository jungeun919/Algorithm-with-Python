# 10 12 3 9
# 3 13 23 33 43 ...
# 9 21 33 45 ...
# k=33
# (33-3)%10=0 (k-x)%M=0
# (33-9)%12=0 (k-y)%N=0

import sys

input = sys.stdin.readline

T = int(input())

def calc(M, N, x, y):
	k = x
	while k <= M * N:
		if (k-y) % N == 0:
			return k
		k += M
	return -1

for _ in range(T):
	M, N, x, y = map(int, input().split())
	print(calc(M, N, x, y))
