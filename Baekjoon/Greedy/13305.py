# n = int(input())

# dist = list(map(int, input().split()))
# cost = list(map(int, input().split()))

# min_cost_index = cost.index(min(cost))
        
# res = dist[0] * cost[0]

# for i in range(1, n - 1):
#     if i == min_cost_index:
#         res += (sum(dist[1:]) * cost[i])
#         break
#     else:
#         res += (dist[i] * cost[i])
        
# print(res)

n = int(input())

dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

res = dist[0] * cost[0]
min_cost = cost[0]

for i in range(1, n - 1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    res += dist[i] * min_cost
        
print(res)
