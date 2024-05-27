import sys

input = sys.stdin.readline

N = int(input())

calendar = [0] * 366 # 날짜별 일정의 개수

for _ in range(N):
    start, end = map(int, input().split())

    for day in range(start, end+1):
        calendar[day] += 1

row = 0
col = 0
area = 0

for day in calendar:
    if day != 0: # 일정이 있다면
        row = max(row, day)
        col += 1
    else:
        area += row * col
        row = 0
        col = 0
area += row * col

print(area)
