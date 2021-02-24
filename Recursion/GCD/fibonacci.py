# n번째 피보나치 수열 찾기 (인덱스는 0부터 시작)

def fibonacci(n):
    if n <=1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(0)) # 0 (0)
print(fibonacci(1)) # 1 (0, 1)
print(fibonacci(2)) # 1 (0, 1, 1)
print(fibonacci(3)) # 2 (0, 1, 1, 2)
print(fibonacci(10)) # 55 (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)