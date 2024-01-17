import sys

input = sys.stdin.readline

n = int(input())
buy = list(map(int, input().split())) + [0, 0]

cost = 0

for i in range(n):
    if buy[i + 1] > buy[i + 2]:
        buy_two = min(buy[i], buy[i + 1] - buy[i + 2])
        buy[i] -= buy_two
        buy[i + 1] -= buy_two
        cost += buy_two * 5
        
        buy_three = min(buy[i : i + 2])
        buy[i] -= buy_three
        buy[i + 1] -= buy_three
        buy[i + 2] -= buy_three
        cost += buy_three * 7
        
        buy_one = buy[i]
        cost += buy_one * 3
    
    else:
        buy_three = min(buy[i : i + 2])
        buy[i] -= buy_three
        buy[i + 1] -= buy_three
        buy[i + 2] -= buy_three
        cost += buy_three * 7
        
        buy_two = min(buy[i], buy[i + 1])
        buy[i] -= buy_two
        buy[i + 1] -= buy_two
        cost += buy_two * 5
        
        buy_one = buy[i]
        cost += buy_one * 3

print(cost)
