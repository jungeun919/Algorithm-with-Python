# 연속한 숫자의 곱을 구하는 알고리즘 (재귀 호출 사용)

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print(fact(0)) # 1
print(fact(10)) # 3628800