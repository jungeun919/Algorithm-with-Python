# 합집합 : 0 a b
# 두 원소가 같은 집합에 포함되어 있는지 : 1 a b

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

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
    
for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(a, b)
    elif oper == 1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
