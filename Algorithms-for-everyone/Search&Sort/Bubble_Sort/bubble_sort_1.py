# 오름차순 거품 정렬

def bubble_sort(a):
    n = len(a)

    while True:
        changed = False # 자료를 앞뒤로 바꾸었는지 여부
        # 뒤집힌 자료가 있으면 바꾸고 바뀌었다고 표시
        for i in range(0, n-1):
            if a[i] > a[i+1]:
                print(a)
                a[i], a[i+1] = a[i+1], a[i]
                changed = True # 자료가 바뀌었음을 표시

        # 바뀐 적이 없다면 종료
        # 바뀐 적이 있으면 다시 앞에서부터 비교 반복        
        if changed == False:
            return

num_list = [2, 4, 5, 1, 3]
bubble_sort(num_list)
print(num_list)