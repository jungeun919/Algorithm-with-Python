# 20190923 을 출력합니다.
# 아래 기준만 만족하면 됩니다.

# 1. 코드 내에 숫자가 없어야 합니다.
#     - 예) print(20190923)이라고 하시면 안됩니다.
# 2. 파일 이름이나 경로를 사용해서는 안됩니다.
# 3. 시간, 날짜 함수를 사용해서는 안됩니다.
# 4. 에러 번호 출력을 이용해서는 안됩니다.
# 5. input을 이용해서는 안됩니다.

# 이게 뭘 원하는 문젤까...
string='aacddddddddd'
a=string.count('a') #2
b=string.count('b') #0
c=string.count('c') #1
d=string.count('d') #9
print(int(str(a)+str(b)+str(c)+str(d)+str(b)+str(d)+str(a)+str(a+1)))