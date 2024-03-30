# 1~N 까지 연속한 숫자의 합 구하기

def sum(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

print(sum(100))