# 리스트에서 특정 숫자의 위치 찾기

def search_list(a, x):
    n = len(a) # 리스트의 길이
    for i in range(0, n):
        if x == a[i]:
            return i

    return -1

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18)) # 2
print(search_list(v, 10)) # -1