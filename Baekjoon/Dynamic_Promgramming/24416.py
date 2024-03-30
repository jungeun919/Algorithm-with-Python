# 1 1 2 3 5 8 ...

n = int(input())

def fib(n): # 재귀
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def fibonacci(n): # dp
    f = [0] * (n + 1)
    
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    
    return f[n]

print(fibonacci(n), end=" ")
print(n - 2)
