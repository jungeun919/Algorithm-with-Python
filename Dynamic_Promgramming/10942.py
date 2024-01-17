import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())

dp = [[0] * n for _ in range(n)]

for i in range(n): # 길이가 1일때 true
    dp[i][i] = 1

for i in range(n - 1): # 길이가 2일때
    if nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1

for len in range(2, n): # 길이가 3이상일때
    for start in range(n - len):
        end = start + len
        if nums[start] == nums[end] and dp[start + 1][end - 1] == 1:
            dp[start][end] = 1

for _ in range(m):
    start, end = map(int, input().split())
    print(dp[start - 1][end - 1])
