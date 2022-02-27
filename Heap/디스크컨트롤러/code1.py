from heapq import *

def solution(jobs):
    answer, time, i = 0, 0, 0
    end = -1
    heap = []

    while i < len(jobs):
        for job in jobs:
            if end < job[0] <= time:
                heappush(heap, [job[1], job[0]])

        if len(heap) > 0:
            job = heappop(heap)
            end = time
            time += job[0]
            answer += time - job[1]
            i += 1
        else:
            time += 1
    return answer // len(jobs)