# dfs 풀이
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

cards = []
for _ in range(n):
    cards.append(int(input()))

res = set()
visited = [False] * n # 중복 확인
select_arr = []

def select(len): # 선택한 카드 개수
    if len == k:
        res.add(''.join(map(str, select_arr)))
        return

    for card_idx in range(n):
        if visited[card_idx] == False:
            select_arr.append(cards[card_idx])
            visited[card_idx] = True
            select(len + 1)
            select_arr.pop()
            visited[card_idx] = False

select(0)

print(len(res))

# 내장함수 풀이
from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

cards = []
for _ in range(n):
    cards.append(input().rstrip())

res = set()

for select_card in permutations(cards, k):
    res.add(''.join(select_card))

print(len(res))
