# 재귀 호출을 이용해 1~N 까지의 합 구하기

def fact_sum(n):
    if n == 0:
        return 0
    return n + fact_sum(n-1)

print(fact_sum(10)) # 55