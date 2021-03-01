# 주어진 동전 n개 중에 가짜 동전을 찾아내는 알고리즘 (이분 탐색)

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
    # 종료 조건
    if left == right:
        return left

    # left ~ right에 놓인 동전을 두 그룹으로 나눔
    # 동전 수가 홀수면 두 그룹으로 나누고 한 개가 남음
    half = (right - left + 1) // 2
    g1_left = left
    g1_right = left + half - 1
    g2_left = left + half
    g2_right= g2_left + half - 1

    result = weigh(g1_left, g1_right, g2_left, g2_right)

    if result == -1:
        return find_fakecoin(g1_left, g1_right)
    elif result == 1:
        return find_fakecoin(g2_left, g2_right)
    else:
        return right # 그룹으로 나뉘지 않은 나머지 한 개가 가짜 동전

n = 100 # 전체 동전 개수
print(find_fakecoin(0, n-1))