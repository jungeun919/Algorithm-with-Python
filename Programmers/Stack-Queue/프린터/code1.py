def solution(priorities, location):
    answer = 0
    max_p = max(priorities)
    
    while True:
        item = priorities.pop(0)
        if max_p == item:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
                max_p = max(priorities)
        else:
            priorities.append(item)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer