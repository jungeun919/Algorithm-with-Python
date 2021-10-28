# 새 학기를 맞아 호준이네 반은 반장 선거를 하기로 했습니다.
# 그런데 표를 하나씩 개표하는 과정이 너무 번거롭게 느껴진 당신은 학생들이 뽑은 후보들을 입력받으면 뽑힌 학생의 이름과 받은 표 수를 출력하는 프로그램을 작성하기로 하였습니다.

# >> 입력
# 원범 원범 혜원 혜원 혜원 혜원 유진 유진

# >> 출력
# 혜원(이)가 총 4표로 반장이 되었습니다.

names = input().split()
name = set(names) # 중복 제거, 순서x

dict = {}
for i in names:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

max_name = ''
max_count = 1
for i in dict:
    if dict[i] > max_count:
        max_count = dict[i]
        max_name = i
print("%s(이)가 총 %d표로 반장이 되었습니다." % (max_name, max_count))