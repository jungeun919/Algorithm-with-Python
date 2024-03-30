def solution(answers):
    answer = []
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    
    for i in range(len(answers)):
        ans = answers[i]
        if (ans == supo1[i % len(supo1)]):
            score[0] += 1
        if (ans == supo2[i % len(supo2)]):
            score[1] += 1
        if (ans == supo3[i % len(supo3)]):
            score[2] += 1

    for idx, val in enumerate(score):
        if val == max(score):
            answer.append(idx + 1)
    return answer