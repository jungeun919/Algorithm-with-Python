# 공백으로 구분하여 두 숫자 a와 b가 주어지면, a의 b승을 구하는 프로그램을 작성하세요.

print("[방법1] - 제곱 연산자를 이용")
a, b = map(int, input().split())
res1 = a ** b
print(res1)


print("\n[방법2] - 내장 라이브러리인 math의 pow 함수 이용")
import math

a, b = map(int, input().split())
res2 = math.pow(a, b)
print(res2) # float 형식으로 출력