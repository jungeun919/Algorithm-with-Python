s = input()

count = 0
prev = ''

for c in s:
    if c != prev:
        count += 1
        prev = c

print(count // 2)
