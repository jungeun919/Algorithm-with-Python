import sys

input = sys.stdin.readline

l = int(input())
nums = list(map(int, input().split()))
n = int(input())

nums.sort()

if n in nums:
	print(0)
else:
	min_val = 0
	max_val = 0

	for num in nums:
		if num < n:
			min_val = num
		elif num > n and max_val == 0:
			max_val = num
	
	max_val -= 1
	min_val += 1

	print((n - min_val) * (max_val - n + 1) + (max_val - n))
