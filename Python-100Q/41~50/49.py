# 순서가 없는 10개의 숫자가 공백으로 구분되어 주어진다.
# 주어진 숫자들 중 최댓값을 반환하라.

# >> 입력
# 10 9 8 7 6 5 4 3 2 1
# >> 출력
# 10

# print("[방법1]")
# nums = list(map(int, input().split()))

# maxnum = nums[0]
# for i in nums:
#     if i > maxnum:
#         maxnum = i
# print(maxnum)

print("[방법2]")
nums = list(map(int, input().split()))
sort_nums = sorted(nums)
print(sort_nums[-1])