N = int(input())

ingredient = []
for _ in range(N):
    ingredient.append(list(map(int, input().split())))

def dfs(start, depth, count, select):
    global min_diff

    if depth == count: # 설정한 개수만큼 선택
        sour = 1
        bitter = 0
        for i in select:
            sour *= i[0]
            bitter += i[1]
        min_diff = min(min_diff, abs(sour - bitter))
        return

    for i in range(start, N): # 조합 생성
        select.append(ingredient[i])
        dfs(i+1, depth+1, count, select)
        select.pop()

min_diff = int(2e9)
for i in range(1, N+1): # 선택할 개수
    dfs(0, 0, i, [])
print(min_diff)
