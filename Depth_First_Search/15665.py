import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

sequence = []

def dfs():
    if len(sequence) == m:
        print(" ".join(map(str, sequence)))
        return
    
    overlap = -1
    for i in range(n):
        if overlap != nums[i]:
            sequence.append(nums[i])
            overlap = nums[i]
            dfs()
            sequence.pop()

dfs()
