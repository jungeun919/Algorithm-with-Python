n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

sequence = []

def dfs():
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return
    
    for i in nums:
        if i not in sequence:
            sequence.append(i)
            dfs()
            sequence.pop()
            
dfs()
