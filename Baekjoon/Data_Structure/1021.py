from collections import deque

n, m = map(int, input().split())

queue = deque([i for i in range(1, n + 1)])
values = list(map(int, input().split()))

count = 0
for i in range(m):
    find_val = values[i]
    
    while True:
        if queue[0] == find_val:
            queue.popleft()
            break
        else:
            # index 함수 : 값의 위치 반환
            if queue.index(find_val) <= len(queue) // 2:
                queue.rotate(-1)
                count += 1
            else:
                queue.rotate(1)
                count += 1
print(count)
