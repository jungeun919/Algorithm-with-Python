import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    
    for i in [25, 10, 5, 1]:
        print(n // i, end=" ")
        n = n % i
    print()
