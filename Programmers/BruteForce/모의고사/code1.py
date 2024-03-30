def solution(answers):
    answer = []
    supo = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    right = [0,0,0]
    
    for i in range(len(supo)):
        for j in range(len(answers)):
            if answers[j] == supo[i][j % len(supo[i])]:
                right[i] += 1
                
    for idx, score in enumerate(right):
        if score == max(right):
            answer.append(idx + 1)
    return answer