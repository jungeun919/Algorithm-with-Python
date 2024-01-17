import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

sequence = []

def dfs(start):
    if len(sequence) == m:
        print(" ".join(map(str, sequence)))
        return
    
    overlap = -1
    for i in range(start, n):
        if overlap != nums[i]:
            sequence.append(nums[i])
            overlap = nums[i]
            dfs(i)
            sequence.pop()

dfs(0)
