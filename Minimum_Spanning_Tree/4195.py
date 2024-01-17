import sys

input = sys.stdin.readline

def find_parent(node):
    if node != parent[node]:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    
    if x != y:
        parent[y] = x
        friend[x] += friend[y]

T = int(input())

for _ in range(T):
    n = int(input())
    
    parent = {}
    friend = {}
    
    for _ in range(n):
        a, b = input().split()
        
        if a not in parent:
            parent[a] = a
            friend[a] = 1
        if b not in parent:
            parent[b] = b
            friend[b] = 1
        
        union_parent(a, b)
        print(friend[find_parent(a)])
