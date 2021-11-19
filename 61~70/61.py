# 문자열을 입력받고 연속되는 문자열을 압축해서 표현하고싶습니다.

# >> 입력
# aaabbbbcdddd

# >> 출력
# a3b4c1d4

sentence = input()

res = ''
tmp = sentence[0]
count = 0

for i in sentence:
    if i == tmp:
        count += 1
    else:
        res += tmp + str(count)
        tmp = i
        count = 1

res += tmp + str(count)
print(res)