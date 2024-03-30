from collections import deque

n, k = map(int, input().split())

queue = deque()
for i in range(1, n + 1):
    queue.append(i)

res = []
while queue:
    for i in range(k - 1):
        queue.append(queue[0])
        queue.popleft()
    res.append(queue.popleft())

print("<", end="")
print(", ".join(map(str, res)), end="")
print(">")
