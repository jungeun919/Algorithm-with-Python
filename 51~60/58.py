# 원범이는 편의점 아르바이트가 끝난 후 정산을 하고자 합니다.
# 정산을 빨리하고 집에가고 싶은 원범이는 프로그램을 만들려고 합니다.

# 숫자를 입력 받고 천단위로 콤마(,)를 찍어주세요.

# 예를들어, 123456789를 입력받았으면 123,456,789 를 출력해야합니다.

n = int(input())

print(f'{n:,}')

result = format(n, ',')
print(result)