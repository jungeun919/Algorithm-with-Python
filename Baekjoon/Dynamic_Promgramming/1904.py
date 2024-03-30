# ["00", "1"]
# n = 1: 1
# n = 2: 00, 11
# n = 3: 100, 001, 111
# n = 4: 0000, 1100, 1001, 0011, 1111 
# dp[n] = dp[n - 2] + "00", dp[n - 1] + "1"

n = int(input())
dp = [0, 1, 2]

for i in range(3, n + 1):
    dp.append((dp[i - 2] + dp[i - 1]) % 15746)

print(dp[n])
