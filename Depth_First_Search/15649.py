# 1~n 자연수 중에서 중복 없이 m개를 고른 수열
n, m = map(int, input().split())

sequence = []

def dfs():
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, n + 1):
        if i not in sequence:
            sequence.append(i)
            dfs()
            sequence.pop()
            
dfs()
