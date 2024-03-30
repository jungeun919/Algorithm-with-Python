from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        time = 0
        for q in queue:
            time += 1
            if price > q:
                break 
        answer.append(time)        
    return answer