# 일반적인 선택 정렬: 정렬 알고리즘을 정식으로 구현한 프로그램
# 오름차순 선택 정렬

def sel_sort(a):
    n = len(a)

    for i in range(0, n-1): # 0 ~ n-2까지 반복
        # i번 위치부터 끝까지 자료값 중에서 최소값의 위치를 찾음
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        # 찾은 최솟값을 i번 위치로
        a[i], a[min_idx] = a[min_idx], a[i]
        print(a)

num_list = [2, 4, 5, 1, 3]
sel_sort(num_list)
print(num_list)