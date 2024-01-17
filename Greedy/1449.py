n, l = map(int, input().split())
location = list(map(int, input().split()))

location.sort()

start = location[0]
count = 1

for loc in location[1:]:
    if start < loc < start + l:
        continue
    else:
        start = loc
        count += 1

print(count)
