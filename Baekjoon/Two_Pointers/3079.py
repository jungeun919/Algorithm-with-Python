import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # 심사대, 사람 수
time = [] # 각 심사대에서 심사 시간
for _ in range(N):
    time.append(int(input()))

left = min(time)
right = max(time) * M
min_time = right # 모두 심사받는데 걸리는 시간

while left <= right:
    mid = (left + right) // 2
    count = 0 # mid 시간까지 심사받을 수 있는 사람 수

    for i in range(N):
        count += mid // time[i]

    if count >= M:
        right = mid - 1
        min_time = min(min_time, mid)
    else:
        left = mid + 1

print(min_time)
