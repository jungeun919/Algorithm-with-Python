from collections import Counter
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = Counter(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    
    total = 0
    for height, count in trees.items():
        if height > mid:
            total += (height - mid) * count
            
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)
