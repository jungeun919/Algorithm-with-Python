from itertools import product # 모든 조합 계산

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

# sequence = []

# def dfs():
#     if len(sequence) == m:
#         print(' '.join(map(str, sequence)))
#         return
    
#     for num in nums:
#         sequence.append(num)
#         dfs()
#         sequence.pop()
        
# dfs()

res = map(' '.join, product(map(str, nums), repeat=m))
print('\n'.join(res))
