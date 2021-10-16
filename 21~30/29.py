# 진구는 영어 학원 아르바이트를 하고 있습니다.
# 반 아이들은 알파벳을 공부하는 학생들인데 오늘은 대문자 쓰기 시험을 봤습니다.

# 1) 알파벳 하나만을 입력하고 그 알파벳이 대문자이면 YES를 아니면 NO를 출력하는 프로그램을 만들어 주세요.

# 2) 알파벳 여러개를 입력하고 여러개 입력한 것 중 대문자만 출력해주는 프로그램도 만들어보세요.

print("1)")
alphabet = input("알파벳을 입력하세요: ")

if alphabet.isupper():
    print("YES")
else:
    print("no")


print("\n2)")
alphabets = input("알파벳을 여러개 입력하세요(공백으로 구분): ").split(' ')

for i in alphabets:
    if i.isupper():
        print("%c" % i)
