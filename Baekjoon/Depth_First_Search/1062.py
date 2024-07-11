# 시작: anta / 끝: tica
# 무조건 들어가는 글자: a n t i c (5개)

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

words = []
for _ in range(N):
    words.append(input().rstrip())

learn = [False] * 26

for c in ['a', 'n', 't', 'i', 'c']:
    learn[ord(c) - ord('a')] = True

def check_read():
    read_count = 0

    for word in words:
        flag = True
        for c in word:
            if learn[ord(c) - ord('a')] == False:
                flag = False
                break
        if flag == True:
            read_count += 1

    return read_count

def dfs(start_idx, depth):
    global max_read

    if depth == K - 5:
        max_read = max(max_read, check_read())
        return

    for idx in range(start_idx, 26):
        if learn[idx] == False:
            learn[idx] = True
            dfs(idx, depth+1)
            learn[idx] = False

if K < 5:
    print(0)
    exit(0)

if K == 26:
    print(N)
    exit(0)

max_read = 0
dfs(0, 0)
print(max_read)
