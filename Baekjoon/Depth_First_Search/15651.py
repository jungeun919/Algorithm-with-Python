n, m = map(int, input().split())

sequence = []

def dfs():
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, n + 1):
        sequence.append(i)
        dfs()
        sequence.pop()
        
dfs()
