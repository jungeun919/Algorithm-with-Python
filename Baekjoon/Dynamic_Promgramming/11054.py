n = int(input())
arr = list(map(int, input().split()))

reverse_arr = arr[::-1]

increase_dp = [1] * n
decrease_dp = [1] * n

for i in range(n):
    for j in range(i):
        # 증가하는 수열
        if arr[i] > arr[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)

        # 감소하는 수열
        if reverse_arr[i] > reverse_arr[j]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)

decrease_dp = decrease_dp[::-1]

res = []
for i in range(n):
    res.append(increase_dp[i] + decrease_dp[i] - 1)
print(max(res))
