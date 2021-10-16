# 첫 줄에는 학생의 이름이 공백으로 구분되어 입력되고,
# 두번째 줄에는 그 학생의 수학 점수가 공백으로 구분되어 주어집니다.

# 두 개를 합쳐 학생의 이름이 key이고 value가 수학 점수인 딕셔너리를 출력해주세요.

# >> 입력
# Yujin Hyewon
# 70 100
# >> 출력
# {'Yujin': 70, 'Hyewon': 100}

names = input().split() # list 형태로 반환
scores = list(map(int, input().split()))

print("[방법1]")
res = dict(zip(names, scores))
print(res)

print("[방법2]")
res2 = {name:score for name, score in zip(names, scores)}
print(res2)

# zip 함수
# 여러 개의 iterable(리스트, 튜플 같이 반복 가능) 객체를 인자로 받음
# 내장함수로 같은 길이의 리스트를 같은 인덱스끼리 잘라 리스트로 반환
# 길이가 다를 경우 같은 인덱스끼리만 짝지어주고, zip 객체에서 나머지 인덱스는 제외