from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

deq = deque()

for _ in range(n):
    cmd = input().split()
        
    if cmd[0] == "push_front":
        deq.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        deq.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        if not deq:
        # if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif cmd[0] == "pop_back":
        if not deq:
            print(-1)
        else:
            print(deq.pop())
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        if not deq:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif cmd[0] == "back":
        if not deq:
            print(-1)
        else:
            print(deq[-1])
