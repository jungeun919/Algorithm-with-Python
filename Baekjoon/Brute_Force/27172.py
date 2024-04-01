n = int(input())
cards = list(map(int, input().split()))

cards_with_idx = {card: idx for idx, card in enumerate(cards)}
max_card = max(cards)

res = [0] * n

for i in range(n):
    cur_card = cards[i]
    for j in range(cur_card*2, max_card+1, cur_card): # j는 cur_card의 배수
        if j in cards_with_idx:
            idx = cards_with_idx[j]
            res[i] += 1
            res[idx] -= 1

for i in res:
    print(i, end=' ')
