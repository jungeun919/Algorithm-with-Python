def solution(phoneBook):
    hashDict = {}
    answer = True
    
    for phoneNum in phoneBook:
        hashDict[phoneNum] = 1
    
    for phoneNum in phoneBook:
        jubdoo = ""
        for i in phoneNum:
            jubdoo += i
            if jubdoo in hashDict and jubdoo != phoneNum:
                answer = False
                break
    return answer