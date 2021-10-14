# 영하네 반은 국어, 수학, 영어 시험을 보았습니다.
# 영하는 친구들의 평균 점수를 구해주기로 했습니다.

# 공백으로 구분하여 세 과목의 점수가 주어지면
# 전체 평균 점수를 구하는 프로그램을 작성하세요. 단, 소숫점 자리는 모두 버립니다.

# >> 입력
# 20 30 40
# >> 출력
# 30

print("[방법1] - list로 묶었을 경우")
scores = list(map(int, input().split()))
print(scores)
print("평균점수:", round(sum(scores) / 3))

print("\n[방법2] - list로 묶지 않았을 경우")
a, b, c = map(int, input().split())
print(a, b, c)
print("평균점수:", round((a + b + c) / 3))