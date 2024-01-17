import sys

input = sys.stdin.readline

n = int(input())

#   r      g      b
# 1 [0][0] [0][1] [0][2]
# 2 [1][0] [1][1] [1][2]
# 3 [2][0] [2][1] [2][2]

dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))
    
for i in range(1, n):
    dp[i][0] = dp[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = dp[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = dp[i][2] + min(dp[i - 1][0], dp[i - 1][1])
    
print(min(dp[n - 1]))
