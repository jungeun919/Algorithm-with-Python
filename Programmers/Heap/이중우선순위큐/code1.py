def solution(operations):
    answer = []

    for oper in operations:
        if oper[0] == "I":
            answer.append(int(oper[2:]))
        else:
            if len(answer) == 0:
                pass
            elif oper[2] == '-':
                answer.pop(0)
            else:
                answer.pop()
        answer.sort()

    if len(answer) == 0:
        return [0, 0]
    else:
        return [max(answer), min(answer)]