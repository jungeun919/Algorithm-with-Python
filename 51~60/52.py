# 다음 빈 칸을 채워 퀵 정렬을 완성해주세요.

def quickSort(list):
    cnt = len(list)
    if cnt <= 1:
        return list

    mid = list.pop(cnt//2)
    left = []
    right = []
    
    for i in range(cnt-1):
        if list[i] < mid:
            left.append(list[i])
        else:
            right.append(list[i])
    return quickSort(left) + [mid] + quickSort(right)

test = list(map(int, input().split(' ')))
print(quickSort(test))