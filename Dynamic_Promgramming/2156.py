n = int(input())

amount = []
for _ in range(n):
    amount.append(int(input()))

dp = [0] * n

dp[0] = amount[0]
if n >= 2:
    dp[1] = amount[0] + amount[1]
if n >= 3:
    dp[2] = max(dp[1], amount[0] + amount[2], amount[1] + amount[2])

for i in range(3, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + amount[i], dp[i - 3] + amount[i - 1] + amount[i])

print(dp[n - 1])
