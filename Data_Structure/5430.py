from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    func_comb = input()
    size = int(input())
    queue = deque(input().rstrip()[1:-1].split(','))
    
    # deque(['']) 의 길이 -> 1로 취급
    if size == 0:
        queue = deque()
    
    error_flag = False
    rev_flag = 0
    
    for func in func_comb:
        if func == "R":
            rev_flag += 1
        elif func == "D":
            if len(queue) == 0:
                error_flag = True
                break
            else:
                if rev_flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    
    if error_flag == False:
        if rev_flag % 2 == 1:
            queue.reverse()
        print("[" + ",".join(queue) + "]")
    else:
        print("error")
