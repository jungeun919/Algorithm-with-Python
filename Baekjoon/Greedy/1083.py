import sys

input = sys.stdin.readline

N = int(input()) # 배열 크기
arr = list(map(int, input().split()))
S = int(input()) # 최대 교환 횟수

for i in range(N):
    if S <= 0:
        break

    max_num = max(arr[i : min(N, i+S+1)])
    max_idx = arr.index(max_num)

    for j in range(max_idx, i, -1):
        arr[j], arr[j-1] = arr[j-1], arr[j]
    S -= (max_idx - i)

for num in arr:
    print(num, end=" ")
