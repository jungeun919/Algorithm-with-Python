n, k = map(int, input().split())

def dfs(nums):
	global count

	if sum(nums) > n:
		return
	if sum(nums) == n:
		count += 1
		if count == k:
			print('+'.join(map(str, nums)))
			exit(0)
	
	for i in range(1, 4):
		nums.append(i)
		dfs(nums)
		nums.pop()

count = 0
dfs([])
print(-1)
