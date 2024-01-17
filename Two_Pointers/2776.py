import sys

input = sys.stdin.readline

T = int(input())

def binary_search(check_num, note1):
    start = 0
    end = len(note1) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if note1[mid] == check_num:
            return 1
        if note1[mid] < check_num:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for _ in range(T):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))
    
    note1.sort()
    
    for check_num in note2:
        print(binary_search(check_num, note1))
