def solution(clothes):
    hashDict = {}
    
    for cloth, type in clothes:
        hashDict[type] = hashDict.get(type, 0) + 1
        
    answer = 1
    for type in hashDict:
        answer *= (hashDict[type] + 1)
    return answer - 1