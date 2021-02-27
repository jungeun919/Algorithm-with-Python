# 쉽게 설명한 병합 정렬
# 오름차순 병합 정렬

def merge_sort(a):
    n = len(a)

    # 종료 조건
    if n <= 1:
        return a

    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    # 두 그룹을 하나로 병합
    result = []
    while g1 and g2: # 두 그룹에 모두 자료가 남아 있는 동안 반복
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    # 아직 남아 있는 자료들을 결과에 추가
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

num_list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(num_list))