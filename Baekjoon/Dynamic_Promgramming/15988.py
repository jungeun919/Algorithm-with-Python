import sys

input = sys.stdin.readline

T = int(input())

dp = [0] * 1000001
dp[1] = 1 # 1
dp[2] = 2 # (1,1), 2
dp[3] = 4 # (1,1,1), (1,2), (2,1), 3
dp[4] = 7 # (1,1,1,1), (1,1,2), (1,2,1), (2,1,1), (2,2), (1,3), (3,1)

for i in range(5, 1000001):
    dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1000000009

for _ in range(T):
    n = int(input())
    print(dp[n])
