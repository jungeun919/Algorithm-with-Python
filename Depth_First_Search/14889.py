n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
visited = [False] * n

diff = int(1e9)

def dfs(count, idx):
    global diff
    
    if count == n // 2:
        team1 = 0
        team2 = 0
        for i in range(n):
            for j in range(n):
                if visited[i] == True and visited[j] == True:
                    team1 += graph[i][j]
                elif visited[i] == False and visited[j] == False:
                    team2 += graph[i][j]
        diff = min(diff, abs(team1 - team2))
        return
    
    for i in range(idx, n):
        if visited[i] == False:
            visited[i] = True
            dfs(count + 1, i + 1)
            visited[i] = False

dfs(0, 0)

print(diff)
