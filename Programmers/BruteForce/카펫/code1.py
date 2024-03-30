def solution(brown, yellow):
    total = brown + yellow

    for i in range(total, 2, -1):
        if total % i == 0:
            brown_x = i
            brown_y = total // i
            if yellow == (brown_x - 2) * (brown_y - 2):
                return [brown_x, brown_y]

# def solution(brown, yellow):
#     answer = []

#     for i in range(1, yellow + 1):
#         if yellow % i == 0:
#             yellow_x = yellow // i
#             yellow_y = i
#             if (yellow_x * 2) + (yellow_y * 2) + 4 == brown:
#                 answer.append(yellow_x + 2)
#                 answer.append(yellow_y + 2)
#                 break
#     return answer