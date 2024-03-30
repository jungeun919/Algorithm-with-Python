def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
        
    for com in completion:
        sumHash -= hash(com)
        
    return hashDict[sumHash]