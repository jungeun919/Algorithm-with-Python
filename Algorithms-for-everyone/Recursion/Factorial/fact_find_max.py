# 재귀 호출을 이용한 최댓값 찾기

def find_max(a, n):
    if n == 1:
        return a[0]
    max_n = find_max(a, n-1)

    if max_n > a[n-1]:
        return max_n
    else:
        return a[n-1]

value = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(value, len(value)))