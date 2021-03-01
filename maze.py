# 미로 찾기 프로그램 (그래프 탐색)

# start
# ↓
# ■■■■■■■■■■■■■■■■■  
# ■ a ■ b   c   d ■
# ■   ■     ■■■■■■■
# ■ e ■ f   g   h ■
# ■   ■     ■■■   ■
# ■ i ■ j   k ■ l ■
# ■       ■   ■   ■
# ■ m   n ■ o ■ p ■
# ■■■■■■■■■■■■■■■■■
#               ↓
#               end

def solve_maze(g, start, end):
    qu = [] # 앞으로 처리해야 할 이동 경로를 큐에 저장
    done = set() # 이미 큐에 추가한 꼭짓점들을 집합에 기록 (중복 방지)

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        v = p[-1] # 큐에 저장된 이동 경로의 마지막 문자가 현재 처리해야 할 꼭짓점
        if v == end:
            return p

        for x in g[v]:
            if x not in done:
                qu.append(p + x)
                done.add(x)

    return "?"

# 미로 정보
maze = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l']
}

print(solve_maze(maze, 'a', 'p'))