def solution(array, commands):
    answer = []
    
    for i in commands:
        new_array = array[i[0] - 1 : i[1]]
        new_array.sort()
        answer.append(new_array[i[2] - 1])
    return answer