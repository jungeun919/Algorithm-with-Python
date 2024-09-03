import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

arr = []

while A and B:
	maxA = max(A)
	maxB = max(B)
	maxIdxA = A.index(maxA)
	maxIdxB = B.index(maxB)

	if maxA == maxB:
		arr.append(maxA)
		A = A[maxIdxA + 1 : ]
		B = B[maxIdxB + 1 : ]
	elif maxA > maxB:
		A.pop(maxIdxA)
	else:
		B.pop(maxIdxB)

if arr:
	print(len(arr))
	print(" ".join(map(str, arr)))
else:
	print(0)
