import heapq
import sys

input = sys.stdin.readline

n = int(input())

class_list = []
for _ in range(n):
    start, end = map(int, input().split())
    class_list.append([start, end])

class_list.sort()

class_queue = [] # 끝나는 시간 저장
heapq.heappush(class_queue, class_list[0][1])

for i in range(1, n):
    if class_list[i][0] >= class_queue[0]:
        heapq.heappop(class_queue)
    heapq.heappush(class_queue, class_list[i][1])

print(len(class_queue))
