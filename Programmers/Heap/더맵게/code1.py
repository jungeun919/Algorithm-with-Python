from heapq import *

def solution(scoville, k):
    heapify(scoville)
    
    count = 0
    while scoville[0] < k:
        if len(scoville) >= 2:
            heappush(scoville, heappop(scoville) + (heappop(scoville) * 2))
            count += 1
        else:
            return -1
    return count