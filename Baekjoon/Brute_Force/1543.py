word = input()
search = input()

count = 0
i = 0
while i <= len(word) - len(search):
    if word[i : i + len(search)] == search:
        count += 1
        i += len(search)
    else:
        i += 1

print(count)
