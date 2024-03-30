n = int(input())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
    
for i in range(1, n): # 행
    for j in range(len(triangle[i])): # 열
        if j == 0: # 왼쪽 끝
            triangle[i][j] += triangle[i - 1][j]
        elif j == i: # 오른쪽 끝
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    
print(max(triangle[n - 1]))
