import sys

input = sys.stdin.readline

n, c = map(int, input().split())

loc = []
for _ in range(n):
    loc.append(int(input()))

loc.sort()

start = 1
end = loc[n - 1] - loc[0]
res = 0

while start <= end:
    dist = (start + end) // 2
    
    count = 1
    current = loc[0]
    
    for i in range(1, n):
        if loc[i] >= current + dist:
            count += 1
            current = loc[i]
    
    if count >= c: # 간격 넓히기
        start = dist + 1
        res = dist
    else: # 간격 좁히기
        end = dist - 1
        
print(res)
