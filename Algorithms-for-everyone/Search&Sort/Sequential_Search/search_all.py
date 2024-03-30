# 리스트에서 특정 숫자의 위치를 전부 찾기

def search_list(a, x):
    n = len(a)
    result = []

    for i in range(0, n):
        if x == a[i]:
            result.append(i)

    return result

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18)) # [2]
print(search_list(v, 33)) # [3, 6]
print(search_list(v, 10)) # []