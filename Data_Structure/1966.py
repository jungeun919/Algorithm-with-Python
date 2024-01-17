import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # loc : 몇 번째로 인쇄되었는지 궁금하나 문서가 현재 몇 번째에 놓여있는지
    n, loc = map(int, input().split())
    queue = list(map(int, input().split()))
    
    count = 0
    while loc >= 0:
        if queue[0] == max(queue):
            del queue[0]
            loc -= 1 # 제일 앞에 있고, max 값이면 -> -1로 while 빠져나감
            count += 1
        else:
            queue.append(queue[0])
            del queue[0]
            
            if loc == 0:
                loc = len(queue) - 1
            else:
                loc -= 1
    print(count)
