import sys

input = sys.stdin.readline

T = int(input())

def binary_search(arr, val): # 리스트에서 val 보다 작은 값의 개수 리턴
    start = 0
    end = len(arr) - 1

    count = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < val:
            count = mid + 1
            start = mid + 1
        else:
            end = mid - 1
    return count

for _ in range(T):
    N, M = map(int, input().split()) # A, B의 수
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    count = 0
    for a in A:
        if a > B[0]:
            count += binary_search(B, a)
    print(count)
