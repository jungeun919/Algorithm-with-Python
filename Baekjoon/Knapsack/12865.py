# python dictionary 자료구조 이용
n, k = map(int, input().split())

stuff = []
for _ in range(n):
    stuff.append(list(map(int, input().split())))

stuff.sort(reverse=True)

bag = {0: 0} # {value: weight}

for weight, value in stuff:
    temp = {}
    for bag_value, bag_weight in bag.items():
        next_bag_value = bag_value + value
        next_bag_weight = bag_weight + weight

        if bag.get(next_bag_value, k+1) > next_bag_weight:
            temp[next_bag_value] = next_bag_weight
    bag.update(temp)
print(max(bag.keys()))

# knapsack 알고리즘 이용
# n, k = map(int, input().split())
#
# stuff = [[0, 0]]
# for _ in range(n):
#     stuff.append(list(map(int, input().split()))) # [weight, value]
#
# knapsack = [[0] * (k+1) for _ in range(n+1)]
#
# for i in range(1, n+1): # 탐색할 물건의 인덱스
#     for j in range(1, k+1): # 현재 넣을 수 있는 최대 무게
#         weight = stuff[i][0]
#         value = stuff[i][1]
#
#         if weight > j:
#             knapsack[i][j] = knapsack[i-1][j]
#         else:
#             knapsack[i][j] = max(knapsack[i-1][j], value + knapsack[i-1][j-weight])
#
# print(knapsack[n][k])
