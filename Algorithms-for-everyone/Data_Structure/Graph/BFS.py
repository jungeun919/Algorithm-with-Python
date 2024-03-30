# 그래프 탐색: 너비 우선 탐색 (Breadth First Search)

def bfs(g, start):
    qu = [] # 앞으로 처리해야 할 꼭짓점을 큐에 추가
    done = set() # 이미 큐에 추가한 꼭짓점들을 집합에 기록 (중복 방지)

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)

# 그래프 정보
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

bfs(graph, 1)