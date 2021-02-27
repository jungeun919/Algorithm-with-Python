# 정렬된 리스트에서 특정 숫자 위치 찾기 (이분 탐색과 재귀 호출)

def binary_search_sub(a, x, start, end):
    # 종료 조건
    if start > end:
        return -1

    mid = (start + end) // 2
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search_sub(a, x, mid+1, end)
    else:
        return binary_search_sub(a, x, start, end-1)

    return -1 # 찾지 못했을 때

def binary_search(a, x):
    return binary_search_sub(a, x, 0, len(a)-1)

num_list = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(num_list, 36)) # 5
print(binary_search(num_list, 50)) # -1