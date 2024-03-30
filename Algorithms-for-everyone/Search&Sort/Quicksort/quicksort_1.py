# 쉽게 설명한 퀵 정렬
# 오름차순 퀵 정렬

def quick_sort(a):
    n = len(a)

    # 종료 조건
    if n <= 1:
        return a

    # 기준 값을 정하고 기준에 맞춰 그룹을 나누는 과정
    pivot = a[-1] # 마지막 값을 기준 값으로 정함
    g1 = []
    g2 = []

    for i in range(0, n-1): # 마지막 값은 기준 값이므로 제외 (0 ~ n-2까지)
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])

    # 각 그룹에 대해 재귀 호출로 퀵 정렬을 한 후
    # 기준 값과 합쳐 하나의 리스트로 결괏값 반환
    return quick_sort(g1) + [pivot] + quick_sort(g2)

num_list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(num_list))