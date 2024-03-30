from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

count = Counter(nums)

res = [-1] * n
stack = []

for i in range(n):
    while (len(stack) > 0) and (count[nums[stack[-1]]] < count[nums[i]]):
        index = stack.pop()
        res[index] = nums[i]
    stack.append(i)

for i in res:
    print(i, end=" ")
