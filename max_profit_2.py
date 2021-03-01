# 주어진 주식 가격을 보고 얻을 수 있는 최대 수익을 구하는 알고리즘
# 주식을 파는 날을 기준으로 설정

def max_profit(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]

    for i in range(1, n):
        # 지금까지의 최솟값에 주식을 사서 i날에 팔 때의 수익
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]

    return max_profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock)) # 2400 (j: 10200, i: 7800)