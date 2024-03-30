import sys

input = sys.stdin.readline

def dfs(count, idx):
	if count == 6:
		print(*res)
		return
	
	for i in range(idx, k):
		res.append(s[i])
		dfs(count + 1, i + 1)
		res.pop()

while True:
	nums = list(map(int, input().split()))
	k = nums[0]
	s = nums[1:]

	if k == 0:
		break

	res = []
	dfs(0, 0)
	print()
