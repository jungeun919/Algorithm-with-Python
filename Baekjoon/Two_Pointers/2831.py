N = int(input())

# 양수일 경우: 자신보다 키가 큰 사람
# 음수일 경우: 자신보다 키가 작은 사람
male = list(map(int, input().split()))
female = list(map(int, input().split()))

male.sort()
female.sort()

res = 0
mp, fp = 0, N-1

# 음수-양수 / 양수-음수 가능
# 음수의 절댓값이 더 커야함
while mp < N and fp >= 0:
    if male[mp] < 0 and female[fp] > 0:
        if abs(male[mp]) > abs(female[fp]):
            res += 1
            mp += 1
            fp -= 1
        else:
            fp -= 1

    elif male[mp] > 0 and female[fp] < 0:
        if abs(male[mp]) < abs(female[fp]):
            res += 1
            mp += 1
            fp -= 1
        else:
            fp -= 1

    else:
        if male[mp] < 0:
            mp += 1
        elif female[fp] > 0:
            fp -= 1

print(res)
