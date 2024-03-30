import sys
import math

input = sys.stdin.readline

n = int(input())

stars = []
for _ in range(n):
    stars.append(list(map(float, input().split())))

parent = [i for i in range(n + 1)] # 자기자신을 부모로 초기화

def find_parent(node):
    if node != parent[node]:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    
    if x > y: # 작은 쪽이 부모로
        parent[x] = y
    else:
        parent[y] = x

def get_distance(x1, x2, y1, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

dist = []
for i in range(n - 1):
    for j in range(i + 1, n):
        distance = get_distance(stars[i][0], stars[j][0], \
                                stars[i][1], stars[j][1])
        dist.append([distance, i, j])

dist.sort()

res = 0
for d in dist:
    distance, x, y = d
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        res += distance
print(round(res, 2))
