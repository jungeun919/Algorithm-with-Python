def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for part, com in zip(participant, completion):
        if part != com:
            return part
    return participant[-1]