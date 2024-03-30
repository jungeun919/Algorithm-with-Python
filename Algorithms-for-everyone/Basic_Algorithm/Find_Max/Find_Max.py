# 최댓값 구하기

def find_max(a):
    n = len(a)
    max_value = a[0]

    for i in range(1, n):
        if a[i] > max_value:
            max_value = a[i]
        return max_value

value = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(value))