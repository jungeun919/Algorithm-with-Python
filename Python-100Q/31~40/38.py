# 호준이는 아르바이트로 영어 학원에서 단어 시험지를 채점하는 일을 하고 있다.
# 호준이가 일하는 학원은 매번 1위부터 3위까지의 학생에게 상으로 사탕을 준다.
# 그런데 오늘은 마침 사탕이 다 떨어져서 호준이가 채점을 하고 점수를 보내면, 당신이 아이들의 숫자만큼 사탕을 사러 가기로 했다.

# 학생들의 점수를 공백으로 구분하여 입력받는다.
# 1위~ 3위 학생은 여러명일 수 있고 1~3위 학생 중 중복되는 학생까지 포함하여 사탕을 사기로 한다.

# - 학생 수는 4명 이상입니다.
# - 숫자 외에 다른 값은 입력되지 않습니다.

# 점수입력 : 97 86 75 66 55 97 85 97 97 95
# 출력 : 6

scores = list(map(int, input().split()))

count = 0
if len(set(scores)) <= 3: # 4위 이후 존재x
    count = len(scores)
else:
    deduplication_list = list(set(scores))
    max_point = sorted(deduplication_list, reverse=True)[2] # 3위 점수
    
    for i in scores:
        if i >= max_point:
            count += 1
print(count)