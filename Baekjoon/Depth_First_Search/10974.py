n = int(input())

sequence = []

def dfs():
    if len(sequence) == n:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, n + 1):
        if i not in sequence:
            sequence.append(i)
            dfs()
            sequence.pop()

dfs()
