# 11 = 3*3 + 1*1 + 1*1 -> 3개항
# 11 = 2*2 + 2*2 + 1*1 + 1*1 + 1*1 -> 5개항

n = int(input())

# 1의 거듭제곱으로 구성되었을 때 항의 개수
dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if j * j > i:
            break
        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i - j*j] + 1

print(dp[n])
