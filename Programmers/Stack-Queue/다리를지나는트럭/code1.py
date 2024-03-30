def solution(bridge_length, weight, truck_weights):
    answer = 0
    cross = [0] * bridge_length
    
    while len(cross):
        answer += 1
        cross.pop(0)
        if truck_weights:
            if sum(cross) + truck_weights[0] <= weight:
                cross.append(truck_weights.pop(0))
            else:
                cross.append(0)
    return answer