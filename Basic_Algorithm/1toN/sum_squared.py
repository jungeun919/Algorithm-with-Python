# 1~N 까지 제곱된 숫자의 합 구하기

# 1. 공식 이용 x
def sum_squared(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i * i
    return sum

print(sum_squared(10))

# 2. 공식 이용
# n * (n+1) * (2n+1) / 6
def sum_squared_2(n):
    return n * (n+1) * (2*n + 1) // 6

print(sum_squared_2(10))