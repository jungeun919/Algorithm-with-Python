n = int(input())

nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_res = -int(1e9)
min_res = int(1e9)

def dfs(i, add, sub, mul, div, res):
    global max_res, min_res
    
    if i == n:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return
    
    if add > 0:
        dfs(i + 1, add - 1, sub, mul, div, res + nums[i])
    if sub > 0:
        dfs(i + 1, add, sub - 1, mul, div, res - nums[i])
    if mul > 0:
        dfs(i + 1, add, sub, mul - 1, div, res * nums[i])
    if div > 0:
        dfs(i + 1, add, sub, mul, div - 1, int(res / nums[i]))

dfs(1, add, sub, mul, div, nums[0])

print(max_res)
print(min_res)
