# 정렬된 리스트에서 특정 숫자 위치 찾기 (이분 탐색)

def binary_search(a, x):
    start = 0
    end = len(a)-1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid -1

    return -1 # 찾지 못했을 때

num_list = [1, 4, 9, 16, 25, 36, 48, 64, 81]
print(binary_search(num_list, 36)) # 5
print(binary_search(num_list, 50)) # -1