N = int(input())

top = list(map(int, input().split()))

res = [0] * N
stack = []

for i in range(N):
    while stack:
        if top[i] < stack[-1][1]:
            res[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, top[i]]) # [인덱스, 높이]

for i in res:
    print(i, end=' ')
