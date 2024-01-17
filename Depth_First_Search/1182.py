n, s = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
sequence = []

def dfs(start):
    global count
    
    if len(sequence) > 0 and sum(sequence) == s:
        count += 1
    
    for i in range(start, n):
        sequence.append(nums[i])
        dfs(i + 1)
        sequence.pop()

dfs(0)

print(count)
