# 문자열이 주어지면 대문자와 소문자를 바꿔서 출력하는 프로그램을 작성하세요.

# >> 입력
# AAABBBcccddd
# >> 출력
# aaabbbCCCDDD

s = input()
res = []

for i in s:
    if i.isupper():
        res.append(i.lower())
    else:
        res.append(i.upper())

for i in res:
    print(i, end='')