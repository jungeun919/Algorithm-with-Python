from heapq import *

def solution(operations):
    answer = []
    heap = []

    for oper in operations:
        if oper[0] == "I":
            heappush(heap, int(oper[2:]))
        else:
            if len(heap) == 0:
                pass
            elif oper[2] == '-':
                heappop(heap)
            else:
                heap = nlargest(len(heap), heap)[1:]
                heapify(heap)

    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), min(heap)]