s = input()

for i in range(len(s)):
    word = s[i:]
    if word == word[::-1]:
        print(len(s) + i)
        break
