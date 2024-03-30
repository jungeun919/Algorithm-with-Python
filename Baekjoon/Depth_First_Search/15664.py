import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

sequence = []
visited = [False] * n

def dfs(start):
    if len(sequence) == m:
        print(" ".join(map(str, sequence)))
        return
    
    overlap = -1
    for i in range(start, n):
        if not visited[i] and overlap != nums[i]:
            visited[i] = True
            sequence.append(nums[i])
            overlap = nums[i]
            dfs(i + 1)
            sequence.pop()
            visited[i] = False

dfs(0)
