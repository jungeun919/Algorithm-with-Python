import heapq
import sys

input = sys.stdin.readline

N = int(input())

classes = []
for _ in range(N):
    _, s, e = map(int, input().split()) # 강의번호, 시작시간, 종료시간
    classes.append([s, e])

classes.sort(key=lambda x: x[0])

rooms = [] # 종료시간
for s, e in classes:
    if rooms and rooms[0] <= s:
        heapq.heappop(rooms) # 가장 작은 원소 제거
    heapq.heappush(rooms, e)
print(len(rooms))
