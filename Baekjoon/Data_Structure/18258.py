from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

queue = deque()

for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif cmd[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
