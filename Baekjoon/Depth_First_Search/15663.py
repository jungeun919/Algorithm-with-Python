import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

sequence = []
visited = [False] * n

def dfs():
    if len(sequence) == m:
        print(" ".join(map(str, sequence)))
        return
    
    overlap = -1 # check
    for i in range(n):
        if not visited[i] and overlap != nums[i]: # check
            visited[i] = True
            sequence.append(nums[i])
            overlap = nums[i] # check
            dfs()
            sequence.pop()
            visited[i] = False

dfs()
