a, b = input().split()

diff = []
for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[j + i]:
            count += 1
    diff.append(count)

print(min(diff))
