# 병합정렬(merge sort)은 대표적인 정렬 알고리즘 중 하나로 다음과 같이 동작합니다.

# 1. 리스트의 길이가 0 또는 1이면 이미 정렬된 것으로 본다. 그렇지 않은 경우에는
# 2. 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
# 3. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
# 4. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.
# (출처 : 위키피디아)

# 다음 코드의 빈칸을 채워 병합정렬을 완성해 봅시다.


def mergeSort(list):
    cnt = len(list)
    if cnt <= 1:
        return list

    mid = cnt // 2
    left = mergeSort(list[:mid])
    right = mergeSort(list[mid:])
    res = []

    while (left and right):
        if (left[0] < right[0]):
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    while left:
        res.append(left.pop(0))
    while right:
        res.append(right.pop(0))
    return res

# test = [180, 145, 165, 45, 170, 175, 173, 171]
test = list(map(int, input().split(' ')))
print(mergeSort(test))