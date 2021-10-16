# 공백으로 구분하여 두 숫자가 주어집니다.
# 첫번째 숫자로 두번째 숫자를 나누었을 때 그 몫과 나머지를 공백으로 구분하여 출력하세요.

# >> 입력
# 10 2
# >> 출력
# 5 0

print("[방법1] - 연산자를 이용")
a, b = map(int, input().split())

res = a // b # 몫
left = a % b # 나머지
print(res, left)


print("\n[방법2] - divmod 함수 이용")
a, b = map(int, input().split())

res, left = divmod(a, b) # divmod의 결과는 tuple 형식
print(res, left)