n, m = map(int, input().split())

sequence = []

def dfs(start):
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(start, n + 1):
        sequence.append(i)
        dfs(i)
        sequence.pop()
        
dfs(1)
