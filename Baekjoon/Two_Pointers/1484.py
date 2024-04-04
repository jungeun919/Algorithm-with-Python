# G = 현재_몸무게^2 - 이전_몸무게^2
# a^2 - b^2 = (a+b)(a-b) <= G
# a-b는 최소 1이어야 함 -> a+b는 최대 G

G = int(input())

weight = []

start, end = 1, 2
while start + end <= G:
    temp = end**2 - start**2
    if temp == G:
        weight.append(end)
        end += 1
    elif temp < G:
        end += 1
    elif temp > G:
        start += 1

if weight:
    for w in weight:
        print(w)
else:
    print(-1)
