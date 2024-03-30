def solution(brown, yellow):
    total = brown + yellow

    for i in range(total, 2, -1):
        if total % i == 0:
            brown_x = i
            brown_y = total // i
            if (brown_x - 2) * (brown_y - 2) == yellow:
                return [brown_x, brown_y]