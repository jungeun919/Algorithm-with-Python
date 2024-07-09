def solution(bandage, health, attacks):
    attack_dict = {}
    for time, damage in attacks:
        attack_dict[time] = damage
    
    sequence_time = 0 # 연속 성공 시간
    curr_health = health
    end_time = attacks[-1][0]
    
    for t in range(end_time + 1):
        if t in attack_dict:
            sequence_time = 0
            curr_health -= attack_dict[t]
            if curr_health <= 0:
                return -1
        else:
            sequence_time += 1
            curr_health += bandage[1]
            if sequence_time == bandage[0]: # 추가 회복
                curr_health += bandage[2]
                sequence_time = 0
            if curr_health > health: # 최대 체력
                curr_health = health
    
    return curr_health
