import sys

input = sys.stdin.readline

N = int(input()) # 이동하려는 채널
M = int(input()) # 고장난 버튼의 개수
broken = list(input().split())

min_count = abs(100 - N)

for num in range(1000001):
    for i in str(num):
        if i in broken:
            break
    else: # 고장난 버튼이 없는 경우
        min_count = min(min_count, len(str(num)) + abs(num - N))

print(min_count)
