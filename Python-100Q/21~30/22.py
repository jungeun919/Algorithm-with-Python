# 다음 중 변수 i가 6의 배수인지 확인하는 방법으로 올바른 것은?

# 1)  i / 6 == 0
# 2)  i % 6 == 0
# 3)  i & 6 == 0
# 4)  i | 6 == 0
# 5)  i // 6 == 0

print("정답은 2번")
print("%는 나머지를 구하는 연산자")
print("그래서 6으로 나눠서 나머지가 0이면 6의 배수")

# 설명
# 1번 (/): 나눗셈 연산을 할 때 -> float 형태로 출력
# 2번 (%): 나눗셈 연산을 할 때 -> 나머지 구하기
# 3번 (&): Bitwise 연산자 (비트단위의 연산, 2진수로 변환 후) \
#           -> AND 연산, 둘 다 참(1)일때만 True
# 4번 (|): Bitwise 연산자 (비트단위의 연산, 2진수로 변환 후) \
#           -> OR 연산, 둘 중 하나만 참(1)이여도 True
# 5번 (//): 나눗셈 연산을 할 때 -> 몫 구하기