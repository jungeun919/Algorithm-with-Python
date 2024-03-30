# 최솟값 구하기

def find_min(a):
    n = len(a)
    min_value = a[0]

    for i in range(1, n):
        if a[i] < min_value:
            min_value = a[i]
    return min_value

value = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min(value))