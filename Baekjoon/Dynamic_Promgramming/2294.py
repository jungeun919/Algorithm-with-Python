import sys

input = sys.stdin.readline

# n가지 종류, 가치의 합이 k가 되는 경우의 수 (동전의 개수가 최소가 되도록)
n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

# dp[i]: i원을 만들 때 필요한 동전 최소 개수
dp = [10001] * (k+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
