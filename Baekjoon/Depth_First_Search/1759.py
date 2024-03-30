# 암호
# 1) 중복 문자 x
# 2) 최소 한 개의 모음(aeiou) + 최소 두 개의 자음
# 3) 알파벳이 증가하는 순서로 배열

import sys

sys.setrecursionlimit(10**9)

L, C = map(int, input().split())
alpha = list(input().split())

alpha.sort()

def check(word):
    vcount, ccount = 0, 0 # 모음, 자음 개수

    for c in word:
        if c in ['a', 'e', 'i', 'o', 'u']:
            vcount += 1
        else:
            ccount += 1

    if vcount >= 1 and ccount >= 2:
        return True
    return False

def dfs(sequence: list, start_idx: int):
    if len(sequence) == L:
        if check(sequence) == True:
            print("".join(map(str, sequence)))
            return

    for idx in range(start_idx, C):
        if alpha[idx] not in sequence:
            sequence.append(alpha[idx])
            dfs(sequence, idx + 1)
            sequence.pop()

dfs([], 0)
