N = int(input())
height = list(map(int, input().split()))

height.sort()
min_diff = int(4e9)

for i in range(N):
    for j in range(i+3, N): # 사이에 두 원소 존재
        left, right = i+1, j-1

        while left < right:
            diff = (height[i] + height[j]) - (height[left] + height[right])
            if abs(diff) < min_diff:
                min_diff = abs(diff)

            if diff == 0:
                print(0)
                exit(0)
            elif diff < 0:
                right -= 1
            else:
                left += 1

print(min_diff)
