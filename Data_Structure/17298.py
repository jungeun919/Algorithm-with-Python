n = int(input())
nums = list(map(int, input().split()))

res = [-1] * n
stack = [] # 인덱스 저장

for i in range(n):
    while (len(stack) > 0) and (nums[stack[-1]] < nums[i]):
        index = stack.pop()
        res[index] = nums[i]
    stack.append(i)

for i in res:
    print(i, end=" ")
