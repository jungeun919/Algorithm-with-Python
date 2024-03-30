# 은주는 놀이공원 아르바이트를 하고 있습니다.
# 은주가 일하는 놀이공원에서는 현재 놀이공원 곳곳에 숨겨진 숫자 스탬프를 모아 오면 선물을 주는 이벤트를 하고 있습니다.
# 숫자 스탬프는 매일 그 수와 스탬프에 적힌 숫자가 바뀌지만 그 숫자는 항상 연속됩니다.
# 그런데 요즘 다른 날에 찍은 스탬프를 가지고 와 선물을 달라고 하는 손님이 늘었습니다.

# 스탬프에 적힌 숫자가 공백으로 구분되어 주어지면 이 숫자가 연속수인지 아닌지 "YES"와 "NO"로 판별하는 프로그램을 작성하세요.

def check(nums):
    nums = sorted(nums)
    print(nums)
    for i in range(len(nums) - 1):
        if nums[i] + 1 != nums[i+1]:
            return 'NO'
    return 'YES'

nums = list(map(int, input().split(' ')))
print(check(nums))