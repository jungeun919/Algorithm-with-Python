# 문장이 입력되면 거꾸로 출력하는 프로그램을 만들어 봅시다.

# >> 입력
# 거꾸로
# >> 출력
# 로꾸거

sentence = input("문장을 입력하세요: ")

print("[방법1]")
print(sentence[::-1])

print("[방법2]")
for i in range(len(sentence)):
    print(sentence[len(sentence) - 1 - i], end='')