import sys

input = sys.stdin.readline

n, m = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))

# (n+1) * (m+1)
dp = [[0] * (m + 1) for _ in range(n + 1)]

# (r,c) -> (r+1, c), (r, c+1), (r+1, c+1)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = maze[i - 1][j - 1] + \
            max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

print(dp[n][m])
