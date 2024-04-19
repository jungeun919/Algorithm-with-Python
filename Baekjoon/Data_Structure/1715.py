import heapq

N = int(input())

cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

total = 0

while len(cards) >= 2:
    # 가장 작은 묶음 두개를 더해서 다시 큐에 넣음
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    total += a+b
    heapq.heappush(cards, a+b)

print(total)
