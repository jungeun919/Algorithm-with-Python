# 쉽게 설명한 선택 정렬: 정렬 원리를 이해하기 위한 참고용 프로그램
# 오름차순 선택 정렬

# 리스트에서 최솟값의 위치를 돌려주는 함수
def find_min_idx(a):
    n = len(a)
    min_idx = 0

    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = []
    while a: # 리스트에 값이 남아있는 동안 반복
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

num_list = [2, 4, 5, 1, 3]
print(sel_sort(num_list))