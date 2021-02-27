# 쉽게 설명한 삽입 정렬
# 오름차순 삽입 정렬

# 리스트 a에서 v가 들어가야 할 위치를 돌려주는 함수
def find_ins_idx(a, v):
    # 이미 정렬된 리스트 a의 자료를 앞에서부터 차례로 확인한다.
    for i in range(0, len(a)):
        # v값보다 i번 위치에 있는 자료값이 크면 v가 그 바로 앞에 놓여야함
        if v < a[i]:
            return i

    # 적절한 위치를 못 찾았을 때는 v가 a의 모든 자료보다 크다는 뜻이므로 맨 뒤에 삽입
    return len(a)

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value) # 꺼낸 값이 들어갈 적당한 위치 찾기
        result.insert(ins_idx, value) # 찾은 위치에 값 삽입
        print(a, result)
    return result

num_list = [2, 4, 5, 1, 3]
print(ins_sort(num_list))