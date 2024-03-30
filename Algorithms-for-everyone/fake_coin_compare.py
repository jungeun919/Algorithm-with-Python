# 최대 수익 문제에서 사용된 두 알고리즘의 계산 속도 비교하기
# fake_coin_1.py: O(n^2)
# fake_coin_2.py: O(n)

import time
import random

# O(n^2) 알고리즘
def max_profit_slow(prices):
    n = len(prices)
    max_profit = 0

    for i in range(0, n-1):
        for j in range(i+1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit

# O(n) 알고리즘
def max_profit_fast(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]

    for i in range(1, n):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]

    return max_profit

def test(n):
    # 5000 ~ 20000까지의 난수로 테스트 자료 만들기
    a = []
    for i in range(0, n):
        a.append(random.randint(5000, 20000))

    # O(n^2) 알고리즘 테스트
    start = time.time()
    mps = max_profit_slow(a)
    end = time.time()
    time_slow = end - start

    # O(n) 알고리즘 테스트
    start = time.time()
    mpf = max_profit_fast(a)
    end = time.time()
    time_fast = end - start

    # 각각의 알고리즘이 같은 최대 수익 값을 계산해야 함
    print(n, mps, mpf)

    m = 0 # 수행 시간 비율
    if time_fast > 0:
        m = time_slow / time_fast

    print("%d %.5f %.5f %.2f" % (n, time_slow, time_fast, m))

test(1000)
test(10000)