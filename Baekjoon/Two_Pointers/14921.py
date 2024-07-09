N = int(input())
arr = list(map(int, input().split())) # 정렬된 상태

left = 0
right = N-1
res = arr[left] + arr[right] # int(2e8)

while left < right:
    temp = arr[left] + arr[right]
    if temp == 0:
        res = temp
        break

    if abs(temp) < abs(res):
        res = temp
    if temp < 0:
        left += 1
    else:
        right -= 1

print(res)
