# import sys

# input = sys.stdin.readline

# T = int(input())
# n = int(input())
# A = list(map(int, input().split()))
# m = int(input())
# B = list(map(int, input().split()))

# sumA = []
# for s in range(n):
# 	for e in range(s, n):
# 		sumA.append(sum(A[s : e+1]))

# sumB = []
# for s in range(m):
# 	for e in range(s, m):
# 		sumB.append(sum(B[s : e+1]))

# sumB.sort()
# count = 0

# for i in range(len(sumA)):
# 	temp = T - sumA[i]
# 	count += sumB.count(temp)

# print(count)


import sys

input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sumA = {}
for s in range(n):
	sum = 0
	for e in range(s, n):
		sum += A[e]
		if sum in sumA:
			sumA[sum] += 1
		else:
			sumA[sum] = 1

count = 0

for s in range(m):
	sum = 0
	for e in range(s, m):
		sum += B[e]
		temp = T - sum
		if temp in sumA:
			count += sumA[temp]

print(count)
