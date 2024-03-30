# 일반적인 퀵 정렬
# 내림차순 퀵 정렬

def quick_sort_sub(a, start, end):
    # 종료 조건
    if end - start <= 0:
        return

    # 기준 값을 정하고 기준 값에 맞춰 각 자료의 위치를 맞춤
    # [기준 값보다 작은 값들, 기준 값, 기준 값보다 큰 값들]
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] >= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]

    # 재귀 호출 부분
    quick_sort_sub(a, start, i-1)
    quick_sort_sub(a, i+1, end)

# 리스트 전체 (0 ~ len(a)-1)를 대상으로 재귀 호출 함수 호출
def quick_sort(a):
    quick_sort_sub(a, 0, len(a)-1)

num_list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(num_list)
print(num_list)