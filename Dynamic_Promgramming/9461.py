# P(1) ~ P(10)
# [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
# P(n) = P(n - 3) + P(n - 2)

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    dp = [0, 1, 1, 1]
    
    for i in range(4, n + 1):
        dp.append(dp[i - 3] + dp[i - 2])
    
    print(dp[n])
