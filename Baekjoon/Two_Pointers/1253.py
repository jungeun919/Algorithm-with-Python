n = int(input())
nums = list(map(int, input().split()))

nums.sort()

count = 0

for i in range(n):
    target = nums[i]
    temp = nums[:i] + nums[i+1:]

    left = 0
    right = len(temp) - 1

    while left < right:
        total = temp[left] + temp[right]

        if total == target:
            count += 1
            break

        elif total < target:
            left += 1

        elif total > target:
            right -= 1

print(count)
