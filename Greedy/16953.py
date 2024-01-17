a, b = map(int, input().split())

count = 1

while (b != a): # b->a (top-down)
    temp = b
    if b % 10 == 1: # 1로 끝나는 경우
        b = b // 10
        count += 1
    elif b % 2 == 0:
        b = b // 2
        count += 1
    
    if temp == b: # 두 연산을 수행할 수 없는 경우
        count = -1
        break

print(count)
