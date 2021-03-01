# 주어진 동전 n개 중에 가짜 동전을 찾아내는 알고리즘 (순차 탐색)

# 무게 재기 함수
# a~b < c~d : -1
# a~b = c~d : 0
# a~b > c~d : 1
def weigh(a, b, c, d):
    fake = 29 # 가짜 동전의 위치
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0

def find_fakecoin(left, right):
    for i in range(left+1, right+1):
        # 가장 왼쪽 동전과 나머지 동전을 차례로 비교
        result = weigh(left, left, i, i)
        if result == -1:
            return left
        elif result == 1:
            return i

    # 가짜 동전이 없는 예외 경우
    return -1

n = 100 # 전체 동전 개수
print(find_fakecoin(0, n-1))