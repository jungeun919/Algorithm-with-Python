# 연속한 숫자의 곱을 구하는 알고리즘 (for 반복문 사용)

def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

print(fact(0)) # 1
print(fact(10)) # 3628800