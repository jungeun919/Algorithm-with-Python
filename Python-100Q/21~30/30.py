# 문자 pineapple에는 apple이라는 문자가 숨어 있습니다.
# 원범이는 이렇듯 문자열 속에 숨어있는 문자를 찾아보려고 합니다.

# 입력으로 첫 줄에 문자열이 주어지고 둘째 줄에 찾을 문자가 주어지면 
# 그 문자가 시작하는 index를 반환하는 프로그램을 만들어 주세요

# >> 입력
# pineapple is yummy
# apple
# >> 출력
# 4

letter = input("문자열을 입력하세요: ")
word = input("찾을 문자를 입력하세요: ")

idx1 = letter.find(word)
print("find로 찾았을 때:", idx1)
# 찾는 문자가 없을 경우 -1을 return

idx2 = letter.index(word)
print("index로 찾았을 때:", idx2)
# 찾는 문자가 없을 경우 ValueError: substring not found 오류 발생